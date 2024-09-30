from app import create_app
from time import sleep
from flask import render_template
import threading

app = create_app()
cont = 0
lock = threading.Lock()  # Criar um lock para sincronizar o acesso ao contador

def tarefa():
    global cont
    while True:
        sleep(5)  # Espera 5 segundos
        with lock:
            cont += 1  # Incrementa o contador em uma seção crítica

def startThread():
    thread = threading.Thread(target=tarefa)
    thread.daemon = True
    thread.start()

@app.route('/teste')
def index():
    with lock:
        return render_template("teste.html", cont=cont)  # Lê o valor de cont com segurança

# Inicia a aplicação e o thread de fundo
if __name__ == "__main__":
    startThread()
    app.run(debug=True)
