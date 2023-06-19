from flask import Flask, render_template
app = Flask(__name__)


# Route ->link do site
@app.route("/")
# criar a primeira página
def homepage():
    return render_template('homepage.html')


@app.route("/contatos")
def contatos():
    return render_template('contatos.html')


@app.route("/usuarios/<nome_usuarios>")
def usuarios(nome_usuarios):
    return render_template("usuarios.html", nome_usuarios=nome_usuarios)


# Função-> Oque você quer exibir naquela página
# Templates
# Colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)
