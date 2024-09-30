from app import create_app
from time import sleep
import threading
# chama a função do app que cria tudo
app = create_app()

def tarefa():
    cont = 0
    while True:
        print("it should be good")
        print(cont)
        cont =cont+1
        sleep(5)
def startThread():
    thread = threading.Thread(target=tarefa)
    thread.daemon = True
    thread.start()

# inicia o app 

if __name__ == "__main__":
    startThread()
    app.run()
