from flask import render_template, request, redirect, url_for, jsonify
from models import Operador, Maquina
from forms import SignUpForm, dadosMaquina, cadastroMaquina
from flask_login import current_user, logout_user, login_user, login_required
from flask_socketio import join_room




def register_routes(app, db, socketio):

    @socketio.on("user_join")
    def conectar_operador(id):
        join_room(id)
        print("Operador conectado á sala "+str(id))

    

    @app.route("/painel_controle")
    @login_required
    def painel_controle():
        maquinas = current_user.maquinas
        return render_template("painel_controle.html", maquinas = maquinas)


    @app.route("/retornar_user")
    def retornar_user():
        return current_user
    #routes relacionado aos atributos -----------------------------------------------------
    @app.route("/lista_maquinas_atributos")
    @login_required
    def lista_maquinas_atributos():
        maquinas = Maquina.query.all()
        return render_template("lista_maquinas_atributos.html", maquinas=maquinas)

    #adicionar atributo
    @app.route("/adicionando_atributos/<id>", methods=["GET", "POST"])
    @login_required
    def add_atributo(id):
        form = dadosMaquina()
        maquina = Maquina.query.get(id)
        if form.validate_on_submit():
            
            if any(i == form.nomedado.data for i in maquina.dadosDict):
                return "Já existe não é possivel adicionar"
            else:
                maquina.dadosDict[form.nomedado.data] = 100
                maquina.maxDict[form.msgErroMin.data] = form.minMaquina.data
                maquina.minDict[form.msgErroMax.data] = form.maxMaquina.data
                maquina.tipoMensagemMax.append(form.optionMax.data)
                maquina.tipoMensagemMin.append(form.optionMin.data)

                
                db.session.commit()
                return redirect(url_for("pagina_principal"))
                
        return render_template('adicionar_atributo.html', form=form)  
    #------------------------------------------------------------------------

    @app.route("/retornar_dados")
    @login_required
    def retornar_dados():
        dados =[]
        maquinas = current_user.maquinas
        for i in maquinas:
            dados.append(i.nome)
            dados.append(i.dadosDict)
        return jsonify(dados)

    




    
    #mostra a lista de máquinas para adicionar a relação
    @app.route("/adicionar_relação", methods=["GET", "POST"])
    @login_required
    def add_relacao():
        maquinas = Maquina.query.all()
        return render_template("adicionar_relacao.html", maquinas = maquinas)
    #adiciona a relação de fato
    @app.route("/add_rel<id>", methods=["GET", "POST"])
    @login_required
    def add_rel(id):
        maquina = Maquina.query.filter_by(id = id).first()
        current_user.maquinas.append(maquina)# cria a relação de maquina e usuário
        db.session.commit()
        maquinas = Maquina.query.all()
        return render_template("adicionar_relacao.html", maquinas =maquinas)

    #adicionar maquinas no servidor
    @app.route("/adicionar_maquinas", methods=["GET", "POST"])
    @login_required
    def adicionar_maquinas():
        form = cadastroMaquina()
        if form.validate_on_submit():
            maquina = Maquina(
                nome = form.nome.data,
                dadosDict = {},
                maxDict = {},
                minDict = {}
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
        logout_user()
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

    
    
    
