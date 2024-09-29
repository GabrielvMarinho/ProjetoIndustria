from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

#criando o db
db = SQLAlchemy()
#cria uma função para iniciar o app quando importar
def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static", static_url_path="/")
    #comando para criar a database e escolher o lugar do diretório
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./testdb.db"
    db.init_app(app)
    app.secret_key = "chaveSecreta"
    #iniciando o login_manager
    login_manager = LoginManager()
    login_manager.init_app(app)
    from models import Operador
    @login_manager.user_loader
    def load_user(id):
        return Operador.query.get(id)
    
    #importando todos os routes
    from routes import register_routes
    #chamar as routes para iniciar o código
    register_routes(app, db)
    migrate = Migrate(app, db)
    #retorna o app pronto para ser inicializado
    return app
