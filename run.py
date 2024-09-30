from app import create_app, db
import threading
from random import randint
from flask_socketio import SocketIO
from time import sleep
from models import Maquina
from flask_login import current_user
app = create_app()
socketio = SocketIO(app)


def tarefa():
    while True:
        with app.app_context():
            maquinas = Maquina.query.all()
            for maquina in maquinas:
                for chave in maquina.dadosDict:
                    maquina.dadosDict[chave] = randint(1, 100)
            db.session.commit()
        socketio.emit('atualizar_dados')
        sleep(1)




if __name__ == "__main__":
    thread = threading.Thread(target=tarefa)
    thread.start()
    socketio.run(app, debug=True)

