from flask import Flask, render_template, request
import os

app = Flask(__name__, template_folder='templates') # Força a leitura da pasta

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pagamento', methods=['POST'])
def pagamento():
    nome = request.form.get('nome')
    valor = request.form.get('valor')
    return f"<h1>Obrigado, {nome}!</h1><p>Valor: R$ {valor}</p>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
