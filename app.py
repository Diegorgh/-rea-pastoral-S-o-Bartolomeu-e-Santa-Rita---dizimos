from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Isso obriga o servidor a ler o arquivo que você criou na pasta templates
    return render_template('index.html')

@app.route('/pagamento', methods=['POST'])
def pagamento():
    nome = request.form.get('nome')
    valor = request.form.get('valor')
    # Mensagem simples de sucesso com estilo rápido
    return f"""
    <div style='text-align:center; padding:50px; font-family:serif; background-color:#F8F5F0; height:100vh;'>
        <h1 style='color:#000080;'>Deus ama quem dá com alegria!</h1>
        <p>Obrigado, {nome}. Sua contribuição de R$ {valor} foi registrada.</p>
        <br>
        <button onclick="window.history.back()" style='background:#000080; color:white; border:none; padding:10px 20px; border-radius:5px; cursor:pointer;'>Voltar</button>
    </div>
    """

if __name__ == "__main__":
    # O Render exige que o app rode na porta definida por eles
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
