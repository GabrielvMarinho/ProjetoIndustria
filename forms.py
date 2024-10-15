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

class dadosMaquina(FlaskForm):
    nomedado = StringField("dado")
    minMaquina = IntegerField('Min')
    msgErroMin = StringField('Mensagem de erro')
    optionMin = RadioField('Grau de Importância:', 
                        choices=[('Pequeno', 'Pequeno'), ('Médio', 'Médio'), ('Grande', 'Grande')],
                        validators=[DataRequired()])
    maxMaquina = IntegerField('Max')
    msgErroMax = StringField ('Mensagem de erro')
    optionMax = RadioField('Grau de Importância:', 
                        choices=[('Pequeno', 'Pequeno'), ('Médio', 'Médio'), ('Grande', 'Grande')],
                        validators=[DataRequired()])
    submit = SubmitField('Submit')
