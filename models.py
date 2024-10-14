from app import db
from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy import JSON

from flask_login import UserMixin

operador_maquina = db.Table("operador_maquina",
                            db.Column("operador_id", db.Integer, db.ForeignKey("operador.id"), primary_key=True),
                            db.Column("maquina_id", db.Integer, db.ForeignKey("maquina.id"), primary_key = True)
                            )

class Operador(db.Model, UserMixin):
    __tablename__ = 'operador'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)
    maquinas = db.relationship("Maquina", secondary=operador_maquina, backref=db.backref("operadores", lazy="dynamic"))

class Maquina(db.Model):
    __tablename__ = 'maquina'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.Text, nullable = False)
    dadosDict = db.Column(MutableDict.as_mutable(JSON))
    # maxDict = db.Column(MutableDict.as_mutable(JSON))
    # minDict = db.Column(MutableDict.as_mutable(JSON))


class Notificacao(db.Model):
    __tablename__ = 'notificacao'
    id = db.Column(db.Integer, primary_key=True)
    mensagem = db.Column(db.Text, nullable=False)
    tipoMensagem = db.Column(db.Text, nullable=False)
    idMaquina = db.Column(db.Integer, db.ForeignKey("maquina.id"), nullable=False)
    idOperador = db.Column(db.Integer, db.ForeignKey("operador.id"), nullable=False)

    

    
    

