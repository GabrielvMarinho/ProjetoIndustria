from app import create_app, db
from time import sleep
import threading
from models import Maquina

app = create_app()

def tarefa():
    while True:
        with app.app_context():
            maquina = Maquina(nome="hell yeah")
            db.session.add(maquina)
            db.session.commit()
                
        sleep(5)

if __name__ == "__main__":
    thread = threading.Thread(target=tarefa)
    thread.start()
    app.run()
