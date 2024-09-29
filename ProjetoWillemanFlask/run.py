from app import create_app
# chama a função do app que cria tudo
flask_app = create_app()
# inicia o app
if __name__ == "__main__":
    flask_app.run(host="127.0.0.1", debug=True)
