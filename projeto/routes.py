from flask import render_template, request, redirect, url_for, jsonify
from models import Operador, Maquina
from forms import SignUpForm, dadosMaquina, cadastroMaquina
from flask_login import current_user, logout_user, login_user, login_required
def register_routes(app, db):

   

    @app.route("/adicionando_atributos", methods=["GET", "POST"])
    @login_required
    def add_atributo():
        form = dadosMaquina()
        maquina = Maquina.query.get(2)

        if form.validate_on_submit():
            maquina.dadosDict[form.nomedado.data] = 100

            db.session.commit()
        return render_template('adicionar_dados.html', form=form)  

    
    #mostra a lista de máquinas para adicionar a relação
    @app.route("/adicionar_relação", methods=["GET", "POST"])
    def add_relacao():
        maquinas = Maquina.query.all()
        return render_template("adicionar_relacao.html", maquinas = maquinas)
    
    #adiciona a relação de fato
    @app.route("/add_rel<id>", methods=["GET", "POST"])
    def add_rel(id):
        maquina = Maquina.query.filter_by(id = id).first()
        current_user.maquinas.append(maquina)# cria a relação de maquina e usuário
        db.session.commit()
        maquinas = Maquina.query.all()
        return render_template("adicionar_relacao.html", maquinas =maquinas)

    @app.route("/adicionar_maquinas", methods=["GET", "POST"])
    @login_required
    def adicionar_maquinas():
        form = cadastroMaquina()
        if form.validate_on_submit():
            maquina = Maquina(
                nome = form.nome.data,
                dadosDict = {}
            )
            db.session.add(maquina)
            db.session.commit()
            return redirect(url_for("pagina_principal"))
        return render_template("adicionar_maquinas.html", form=form)
    
    @app.route("/minhas_maquinas")
    @login_required
    def minhas_maquinas():
        maquinas = current_user.maquinas
        return render_template("minhas_maquinas.html", maquinas=maquinas)
    
    @app.route("/pagina_principal")
    @login_required
    def pagina_principal():
        return render_template("pagina_principal.html")
    
    #routes relacionado ao login-----------------------------------------------------
    @app.route("/sair")
    @login_required
    def sair():
        logout_user
        return redirect(url_for("login"))
    
    @app.route('/signup', methods=["GET", "POST"])
    def signup():
        form = SignUpForm()
        if form.validate_on_submit():
            operador = Operador(
                username = form.username.data,
                password = form.password.data,
            )
            
            db.session.add(operador)
            db.session.commit()
            return redirect(url_for("login"))
        return render_template('signup.html', form=form)

    @app.route('/', methods=["GET", "POST"])
    def login():
        form = SignUpForm()
        if form.validate_on_submit():
            nome = form.username.data
            operador = Operador.query.filter_by(username = nome).first()
            if operador:
                if operador.password == form.password.data:
                    login_user(operador)
                    return redirect(url_for("pagina_principal"))
                else:
                    return "errou a senha faca denovo"
            else:
                return "n existe esse usuário"
        return render_template('login.html', form=form)
    #------------------------------------------------------------------------

    
    
    
