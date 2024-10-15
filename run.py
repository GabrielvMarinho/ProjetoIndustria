from app import create_app, db
import threading
from random import randint
from flask_socketio import SocketIO
from time import sleep
from models import Maquina, Notificacao, Operador
from flask_login import current_user
from flask import jsonify


app, socketio = create_app()


def tarefa():
    while True:
        with app.app_context():
            maquinas = Maquina.query.all()
            for maquina in maquinas:
                for (cDados, vDados), (cMax, vMax), (cMin, vMin) in zip(maquina.dadosDict.items(), maquina.maxDict.items(), maquina.minDict.items()):
                # for chave in maquina.dadosDict:
                    dado = randint(1, 100)
                    if dado>50:
                        #criar uma notificação para cada operador
                        operadores = Operador.query.all()
                        for operador in operadores:
                            #checando se o operador possui aquela máquina no conjunto de máquinas
                            if any(maquinax.id == maquina.id for maquinax in operador.maquinas):
                                notificacao = Notificacao(
                                    mensagem = "máquinas "+maquina.nome+" possui um problema: no "+cDados+":"+str(dado),
                                    tipoMensagem = "PERIGOSO",
                                    idMaquina = maquina.id,
                                    idOperador = operador.id
                                )
                                notificacaoDict = {
                                    "mensagem": notificacao.mensagem,
                                    "tipoMensagem": notificacao.tipoMensagem,
                                    "idMaquina": notificacao.idMaquina,
                                    "idOperador": notificacao.idOperador    
                                }
                                socketio.emit('notificacoes',notificacaoDict, room=operador.id)
                                print("msg")

                                db.session.add(notificacao)

                    maquina.dadosDict[cDados] = dado
            db.session.commit()
        socketio.emit('atualizar_dados')
        sleep(5)





if __name__ == "__main__":
    thread = threading.Thread(target=tarefa)
    thread.start()
    socketio.run(app, debug=True)

