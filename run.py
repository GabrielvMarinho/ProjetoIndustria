from app import create_app
# chama a função do app que cria tudo
app = create_app()
# inicia o app 
if __name__ == "__main__":
    app.run()
