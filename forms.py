from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField

class SignUpForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Sign up')

class cadastroMaquina(FlaskForm):
    nome = StringField('nome da maquina')
    submit = SubmitField('criar')

class dadosMaquina(FlaskForm):
    nomedado = StringField("dado")
    submit = SubmitField('criar')

    # minMaquina = IntegerField('Min')
    # msgErro = StringField('Mensagem de erro')
    # maxMaquina = IntegerField('Max')
    # msgErroMax = StringField ('Mensagem de erro')
    # submit = SubmitField('criar')