from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms import RadioField, SubmitField
from wtforms.validators import DataRequired

class SignUpForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Sign up')

class cadastroMaquina(FlaskForm):
    nome = StringField('nome da maquina')
    submit = SubmitField('criar')

class dadosMaquina(FlaskForm):# BIANCA precisa adicionar valor máximo e valor mínimo, tambpem precisa adicionar a msg para cada
    nomedado = StringField("dado")
    minMaquina = IntegerField('Min')
    msgErroMin = StringField('Mensagem de erro')
    maxMaquina = IntegerField('Max')
    msgErroMax = StringField ('Mensagem de erro')
    option = RadioField('Grau de Importância:', 
                        choices=[('1', 'pequeno'), ('2', 'Médio'), ('3', 'Grande')],
                        validators=[DataRequired()])
    submit = SubmitField('Submit')
