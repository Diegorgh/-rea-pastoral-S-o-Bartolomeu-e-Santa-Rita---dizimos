from flask import Flask, render_template, request, redirect
import sqlite3
import os
import urllib.parse

app = Flask(__name__)

# CONFIGURAÇÃO: Coloque o número da igreja aqui (apenas números)
NUMERO_PAGAMENTO = "5511999999999" 

def init_db():
    conn = sqlite3.connect('igreja.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS dizimos 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  nome TEXT, cpf TEXT, valor REAL, data TEXT)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pagamento', methods=['POST'])
def pagamento():
    nome = request.form.get('nome')
    cpf = request.form.get('cpf')
    valor = request.form.get('valor')
    from datetime import datetime
    data_atual = datetime.now().strftime("%d/%m/%Y %H:%M")

    # 1. Grava no Banco de Dados para o seu controle no /admin
    conn = sqlite3.connect('igreja.db')
    c = conn.cursor()
    c.execute("INSERT INTO dizimos (nome, cpf, valor, data) VALUES (?,?,?,?)", 
              (nome, cpf, valor, data_atual))
    conn.commit()
    conn.close()

    # 2. Cria a mensagem do WhatsApp (Comprovativo)
    mensagem = f"🙏 *Comprovativo de Dízimo*\n\nOlá! Eu, *{nome}*, acabei de realizar uma contribuição no valor de *R$ {valor}* através do site oficial.\n\nCPF: {cpf}\nData: {data_atual}\n\nDeus abençoe!"
    texto_url = urllib.parse.quote(mensagem)
    link_whatsapp = f"https://api.whatsapp.com/send?phone={NUMERO_PAGAMENTO}&text={texto_url}"

    # 3. Redireciona o dizimista para o WhatsApp dele
    return redirect(link_whatsapp)

@app.route('/admin')
def admin():
    # Rota secreta para você ver a lista
    conn = sqlite3.connect('igreja.db')
    c = conn.cursor()
    c.execute("SELECT * FROM dizimos ORDER BY id DESC")
    registros = c.fetchall()
    total = sum(r[3] for r in registros)
    conn.close()
    
    # Criamos uma tabela simples para o admin
    tabela_html = "".join([f"<tr><td>{r[4]}</td><td>{r[1]}</td><td>{r[2]}</td><td>R$ {r[3]:.2f}</td></tr>" for r in registros])
    
    return f"""
    <div style='font-family:sans-serif; padding:30px; background-color:#F8F5F0; min-height:100vh;'>
        <h2 style='color:#000080;'>📊 Relatório Geral de Contribuições</h2>
        <table border='1' style='width:100%; border-collapse:collapse; background:white;'>
            <tr style='background:#000080; color:white;'>
                <th>Data</th><th>Nome</th><th>CPF</th><th>Valor</th>
            </tr>
            {tabela_html}
        </table>
        <h3 style='margin-top:20px; color:#000080;'>Total Arrecadado: R$ {total:.2f}</h3>
        <br><a href='/' style='text-decoration:none; color:grey;'>← Voltar ao Site</a>
    </div>
    """

if __name__ == "__main__":
    init_db()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
