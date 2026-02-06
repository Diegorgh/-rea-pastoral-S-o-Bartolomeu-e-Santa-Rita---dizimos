import streamlit as st
import sqlite3
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Dízimos Online", page_icon="⛪")

# Conexão com Banco de Dados SQLite
def init_db():
    conn = sqlite3.connect('igreja.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS dizimos 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  nome TEXT, cpf TEXT, valor REAL, data TEXT)''')
    conn.commit()
    conn.close()

init_db()

# --- INTERFACE ---
st.title("⛪ Sistema de Contribuição")

menu = st.sidebar.selectbox("Navegação", ["Contribuir", "Painel Admin"])

if menu == "Contribuir":
    st.subheader("🙏 Registre sua Gratidão")
    st.write("Preencha os dados abaixo para gerar o seu pagamento.")
    
    with st.form("form_dizimo"):
        nome = st.text_input("Nome Completo")
        cpf = st.text_input("CPF (Apenas números)")
        valor = st.number_input("Valor da Contribuição (R$)", min_value=1.0, step=5.0)
        
        # Botão de Enviar
        submit = st.form_submit_button("Gerar Pagamento PIX")
        
        if submit:
            if nome and cpf and valor > 0:
                # Salva no banco de dados
                conn = sqlite3.connect('igreja.db')
                c = conn.cursor()
                from datetime import datetime
                data_atual = datetime.now().strftime("%d/%m/%Y %H:%M")
                c.execute("INSERT INTO dizimos (nome, cpf, valor, data) VALUES (?,?,?,?)", 
                          (nome, cpf, valor, data_atual))
                conn.commit()
                conn.close()
                
                st.success(f"Obrigado, {nome}! Deus abençoe sua oferta.")
                st.info("Copia o código PIX abaixo para pagar no seu banco:")
                # Exemplo de código PIX estático (pode ser trocado pela sua chave real)
                st.code("00020126360014BR.GOV.BCB.PIX0114SUACHAVEAQUI")
            else:
                st.error("Por favor, preencha todos os campos corretamente.")

elif menu == "Painel Admin":
    st.subheader("📊 Relatório de Contribuições")
    senha = st.text_input("Senha de Acesso", type="password")
    
    if senha == "1234": # Define uma senha simples para você
        conn = sqlite3.connect('igreja.db')
        df = pd.read_sql_query("SELECT * FROM dizimos", conn)
        conn.close()
        
        if not df.empty:
            st.dataframe(df)
            st.write(f"**Total Arrecadado: R$ {df['valor'].sum():.2f}**")
        else:
            st.info("Ainda não há contribuições registradas.")
