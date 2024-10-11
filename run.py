from app import create_app, db
import threading
from random import randint
from flask_socketio import SocketIO
from time import sleep
from models import Maquina, Notificacao, Operador
from flask_login import current_user
app = create_app()
socketio = SocketIO(app)

def tarefa():
    while True:
        with app.app_context():
            maquinas = Maquina.query.all()
            for maquina in maquinas:
                for chave in maquina.dadosDict:
                    dado = randint(1, 100)
                    if dado>95:
                        #criar uma notificação para cada operador
                        operadores = Operador.query.all()
                        for operador in operadores:
                            #checando se o operador possui aquela máquina no conjunto de máquinas
                            if any(maquinax.id == maquina.id for maquinax in operador.maquinas):
                                notificacao = Notificacao(
                                    mensagem = "máquinas "+maquina.nome+" possui um problema: no "+chave+":"+str(dado),
                                    tipoMensagem = "PERIGOSO",
                                    idMaquina = maquina.id,
                                    idOperador = operador.id
                                )
                                
                                id = operador.id
                                print("id do room"+str(id))
                                socketio.emit('atualizar_dadosx', "qwasdasdasdasdasd", room=f'room_{id}')


                                db.session.add(notificacao)

                    maquina.dadosDict[chave] = dado
            db.session.commit()
        socketio.emit('atualizar_dados')
        sleep(1)




if __name__ == "__main__":
    thread = threading.Thread(target=tarefa)
    thread.start()
    socketio.run(app, debug=True)

