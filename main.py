from flask import Flask, render_template, request, session, flash
from classes import *
from random import choice

app = Flask(__name__)
# chave para criptografar as variáveis de sessão
app.secret_key = "LGBSBGKYW#TBRjGJKgkejhrg"

# seleção aleatória da série destaque
serieDestaque = choice(choice(catalogo).series)

@app.route('/')
def home():
    # SE A CHAVE "login" NÃO EXISTIR DENTRO DO DICIONÁRIO session...
    if "login" not in session:
        session["login"] = False
    conteudo = render_template('index.html', parSerieDestaque=serieDestaque, parCatalogo=catalogo)
    return conteudo

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if request.method == "POST":
        if request.form["email"] == "eu@eu.com" and request.form["senha"] == "aaa":
            session["login"]=True
            conteudo = render_template("dashboard.html",parCatalogo=catalogo)
        else:
            # Se errar o login
            flash("Senha ou login inválidos")
            conteudo = render_template("index.html", parSerieDestaque=serieDestaque, parCatalogo=catalogo)
    elif request.method == "GET" and session["login"] == True:        
        # se já fez login pode acessar o painel de gerenciamento
        conteudo = render_template("dashboard.html",parCatalogo=catalogo)
    else:
        # quando chegar nessa rota sem ter feito login:
        flash("Acesso negado")
        conteudo = render_template("index.html", parSerieDestaque=serieDestaque, parCatalogo=catalogo)
    return conteudo

@app.route("/logout")
def logout():
    if "login" in session:
        session["login"] = False    
    serieDestaque = choice(choice(catalogo).series)
    conteudo = render_template('index.html', parSerieDestaque=serieDestaque, parCatalogo=catalogo)
    return conteudo

# rotas de edição de temas
@app.route("/editar-tema/<string:tema_nome>")
def modificar_tema(tema_nome):
    for tema in catalogo:
        if tema.nome == tema_nome:
            conteudo = render_template('modificar_tema.html', tema=tema, catalogo=catalogo)
    return conteudo
@app.route("/editar-tema/processar-<string:tema_nome>", methods=["POST"])
def processar_tema(tema_nome):
    for tema in catalogo:
        if tema.nome == tema_nome:
            tema.nome = request.form["nome_tema"]
            for serie in series:
                if request.form["series"] in serie.titulo:
                    tema.adicionar_serie(serie)
                elif request.form['remover_series'] == serie.titulo:
                    tema.series.remove(serie)
            tema_editado = tema
    conteudo = render_template("processar_form_tema.html", operacao="modificar",tema=tema_editado)
    return conteudo
@app.route("/editar-tema/deletar-<string:tema_nome>", methods=["POST"])
def deletar_tema(tema_nome):
    for tema in catalogo:
        if tema.nome == tema_nome:
            catalogo.remove(tema)
    conteudo = render_template("processar_form_tema.html", operacao="deletar")
    return conteudo

# rota de adição de tema
@app.route('/criar-tema', methods=["POST"])
def add_tema():
    nome = request.form["nome_tema"]
    novo_tema = Tema(nome)
    catalogo.append(novo_tema)
    conteudo = render_template('processar_form_tema.html', operacao="adicionar", tema= novo_tema)
    return conteudo

# rotas de edição de séries
@app.route("/editar-serie/<string:serie_titulo>")
def modificar_serie(serie_titulo):
    for tema in catalogo:
        for serie in tema.series:
            if serie.titulo == serie_titulo:
                conteudo = render_template('modificar_serie.html', serie=serie)
    return conteudo
@app.route("/editar-serie/processar-<string:serie_titulo>", methods=["POST"])
def processar_serie(serie_titulo):
    for tema in catalogo:
        for serie in tema.series:
            if serie.titulo == serie_titulo:
                serie.titulo = request.form["serie_titulo"]
                serie.sinopse = request.form["serie_sinopse"]
                serie.temporadas = request.form["serie_temporadas"]
                serie.avaliacao = request.form["serie_avaliacao"]
                serie.elenco = request.form["serie_elenco"]
                serie_editada = serie
    conteudo = render_template('processar_form_serie.html', serie=serie_editada, operacao="modificar")
    return conteudo
@app.route('/editar-serie/deletar-<string:serie_titulo>', methods=["POST"])
def deletar_serie(serie_titulo):
    for tema in catalogo:
        for serie in tema.series:
            if serie.titulo == serie_titulo:
                tema.series.remove(serie)
                del serie
    conteudo = render_template('processar_form_serie.html', operacao="deletar")
    return conteudo

# EXECUTAR O PROGRAMA (RODAR O SITE)
if __name__ == '__main__':
    app.run(debug=True)