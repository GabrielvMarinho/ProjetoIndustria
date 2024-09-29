from app import create_app
import os
# chama a função do app que cria tudo
flask_app = create_app()
# inicia o app
if __name__ == "__main__":
    flask_app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
