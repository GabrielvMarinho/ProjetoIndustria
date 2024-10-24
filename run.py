from app import create_app, db
import threading
from random import randint
from flask_socketio import SocketIO
from time import sleep
from models import Maquina, Operador
from singleton import Caretaker
app, socketio = create_app()


def tarefa():
    while True:
        with app.app_context():

            operadores = Operador.query.all()
            maquinas = Maquina.query.all()

            for maquina in maquinas:
                for (cDados, vDados), (msgMax, dadoMax),(msgMin, dadoMin), tipoMensagemMax, tipoMensagemMin in zip(maquina.dadosDict.items(), maquina.maxDict.items(), maquina.minDict.items(), maquina.tipoMensagemMax, maquina.tipoMensagemMin):
                    # teste para mandar notificação plo observer:
                    dado = randint(1, 100)
                    
                    #mudando o valor dos dados da máquina em si
                    maquina.dadosDict[cDados] = dado

                    if dado>dadoMax:
                        #criar uma notificação para cada operador
                        operadores = Operador.query.all()
                        for operador in operadores:

                            #checando se o operador possui aquela máquina no conjunto de máquinas
                            if any(maquinax.id == maquina.id for maquinax in operador.maquinas):

                                
                                notificacaoDict = {
                                    "mensagem": "ERRO-> "+maquina.nome+"\nmsg ->"+msgMax+"\ndado:"+cDados+"-"+str(dado),
                                    "tipoMensagem": tipoMensagemMax,
                                    "idMaquina": maquina.id,
                                    "idOperador": operador.id    
                                }
                                
                                socketio.emit('notificacoes',notificacaoDict, room=operador.id)
                                #caretaker chamando seu metodos estatico para criar um memento
                                Caretaker.getInstance().createMemento(maquina)
                    
                    elif dado<dadoMin:

                        #criar uma notificação para cada operador
                        for operador in operadores:
                            #checando se o operador possui aquela máquina no conjunto de máquinas
                            if any(maquinax.id == maquina.id for maquinax in operador.maquinas):
                                notificacaoDict = {
                                    "mensagem": "ERRO-> "+maquina.nome+" possui um problema:\nmsg ->"+msgMin+"\ndado:"+cDados+"-"+str(dado),
                                    "tipoMensagem": tipoMensagemMin,
                                    "idMaquina": maquina.id,
                                    "idOperador": operador.id    
                                }
                                
                                socketio.emit('notificacoes',notificacaoDict, room=operador.id)
                                #caretaker chamando seu metodos estatico para criar um memento

                                Caretaker.getInstance().createMemento(maquina)
                    

                db.session.commit()
            
            for operador in operadores:
                dados = {}
                
                for maquina in operador.maquinas:
                    dados[maquina.id] = list(maquina.dadosDict.values())     

                socketio.emit('atualizar_dados',dados, room=operador.id)

        sleep(5)





if __name__ == "__main__":
    thread = threading.Thread(target=tarefa)
    thread.start()
    socketio.run(app)

