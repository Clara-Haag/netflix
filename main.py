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
        # cria a chave "login" na session e coloca o valor False
        session["login"] = False

    # chamar a template index.html passando pra ela a série destaque e o catálogo 
    conteudo = render_template('index.html', parSerieDestaque=serieDestaque, parCatalogo=catalogo)
    return conteudo

# como essa rota pode chegar vinda de um formulário, precisamos ativar os métodos 
@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    # pode chegar nessa rota vindo de um formulário ou vindo de um link.
    # quando chegar nessa rota vindo de um formulário:
    if request.method == "POST":
        # vamos pegar o que foi preenchido no formulário
        # os campos do formulário ficam armazenados no dicionário request.form
        # as chaves do dicionário são os "name" dos campos do form na template
        # os valores do dicionário são as respostas que a pessoa preencheu nos campos
        if request.form["email"] == "eu@eu.com" and request.form["senha"] == "aaa":
            # Se a pessoa acertar o login, vai alterar a session "login" para True
            # Assim saberemos em qualquer página do site se a pessoa fez login ou não
            session["login"]=True
            # depois do login, chamamos o painel de gerenciamento passando pra ele o catálogo
            conteudo = render_template("dashboard.html",parCatalogo=catalogo)
        else:
            # Se errar o login:
            flash("Senha ou login inválidos")
            conteudo = render_template("index.html", parSerieDestaque=serieDestaque, parCatalogo=catalogo)
    
    # esse elif pertence ao primeiro IF dessa def
    # quando chegar nessa rota via GET (por um link por exemplo) 
    # mas já ter feito login:
    elif request.method == "GET" and session["login"] == True:        
        # se já fez login pode acessar o painel de gerenciamento
        conteudo = render_template("dashboard.html",parCatalogo=catalogo)
    else:
        # quando chegar nessa rota sem ter feito login:
        flash("Acesso negado")
        # não pode acessar o painel, 
        # por isso chamamos a template que mostra a mensagem de erro
        conteudo = render_template("index.html", parSerieDestaque=serieDestaque, parCatalogo=catalogo)

    # depois dos testes de login vai retornar o conteúdo correto:
    return conteudo

@app.route("/logout")
def logout():
    # primeiro verificamos se existe algum login na session
    # caso seja o primeiro acesso ao site e a pessoa digite o endereço do logout,
    # não vai ter a chave "login" dentro da session para alterar.

    # se a chave "login" existir dentro da session...
    if "login" in session:
        # altera o valor de "login" na session e coloca o valor False
        # isso vai efetivar o logout
        session["login"] = False    

    # repete os passos de carregamento da home depois de ter feito logout 
    serieDestaque = choice(choice(catalogo).series)
    conteudo = render_template('index.html', parSerieDestaque=serieDestaque, parCatalogo=catalogo)
    return conteudo


# EXECUTAR O PROGRAMA (RODAR O SITE)
if __name__ == '__main__':
    app.run(debug=True)