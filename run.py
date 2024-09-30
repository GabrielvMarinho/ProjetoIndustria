from app import create_app
from time import sleep
from flask import render_template
import threading

app = create_app()
cont = 0

def tarefa():
    sleep(5)
    cont =cont+1
    return render_template("teste.html", cont=cont)
def startThread():
    thread = threading.Thread(target=tarefa)
    thread.daemon = True
    thread.start()

# chama a função do app que cria tudo
if __name__ == "__main__":
    startThread()
    app.run()
