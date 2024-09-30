from app import create_app, db
from time import sleep
import threading
from models import Maquina

app = create_app()

def tarefa():
    while True:
        # Criação do contexto da aplicação
        with app.app_context():
            maquina = Maquina(
                nome="hell yeah"
            )
            db.session.add(maquina)
            db.session.commit()
        sleep(5)

def startThread():
    thread = threading.Thread(target=tarefa)
    thread.daemon = True
    thread.start()

# Inicia a aplicação e a thread de fundo
if __name__ == "__main__":
    startThread()
    app.run()
