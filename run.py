from app import create_app, db
import threading
from random import randint
app = create_app()

from time import sleep
from models import Maquina

def tarefa():
    while True:
        with app.app_context():
            maquinas = Maquina.query.all()
            for maquina in maquinas:
                for chave in maquina.dadosDict:
                    maquina.dadosDict[chave] = randint(1, 100)
            db.session.commit()
        sleep(5)



if __name__ == "__main__":
    thread = threading.Thread(target=tarefa)
    thread.start()
    app.run(debug=True, use_reloader=False) #tirar no deploy
