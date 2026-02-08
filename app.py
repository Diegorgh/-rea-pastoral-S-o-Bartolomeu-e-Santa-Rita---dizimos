from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    # Isso vai procurar o arquivo dentro da pasta templates
    return render_template('index.html')

@app.route('/pagamento', methods=['POST'])
def pagamento():
    # Aqui o sistema recebe os dados do formulário
    nome = request.form.get('nome')
    valor = request.form.get('valor')
    return f"<h1>Obrigado, {nome}!</h1><p>Processando seu dízimo de R$ {valor}...</p>"

if __name__ == "__main__":
    app.run(debug=True)
