from app import create_app
from time import sleep
import threading
import logging

# Configurar o logging para exibir no console (STDOUT)
logging.basicConfig(level=logging.INFO)

# chama a função do app que cria tudo
app = create_app()

def tarefa():
    cont = 0
    while True:
        logging.info("it should be good")
        logging.info(f"Cont: {cont}")  # Usando logging ao invés de print
        cont += 1
        sleep(5)

def startThread():
    thread = threading.Thread(target=tarefa)
    thread.daemon = True
    thread.start()

# inicia o app
if __name__ == "__main__":
    startThread()
    app.run()
