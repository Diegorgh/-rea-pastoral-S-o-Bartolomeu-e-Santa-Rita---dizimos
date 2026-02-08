import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime

# 1. Configuração da Página e Estilo Profissional
st.set_page_config(page_title="Gestão de Dízimos", page_icon="🙏", layout="wide")

# CSS para customizar as cores e o design
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { 
        background-color: #1a4a7a; 
        color: white; 
        border-radius: 10px; 
        width: 100%;
        height: 3em;
    }
    h1 { color: #1a4a7a; font-family: 'Helvetica'; }
    .css-10trblm { border-radius: 15px; box-shadow: 0px 4px 10px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

# 2. Inicialização do Banco de Dados
def init_db():
    conn = sqlite3.connect('igreja.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS dizimos 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  nome TEXT, cpf TEXT, valor REAL, data TEXT)''')
    conn.commit()
    conn.close()

init_db()

# --- TOPO DO SITE (LOGO E TÍTULO) ---
col_logo, col_tit = st.columns([1, 4])
with col_logo:
    # Substitua pelo link da sua logo real se tiver uma
    st.image("https://cdn-icons-png.flaticon.com/512/3395/3395949.png", width=100) 
with col_tit:
    st.title("Dízimo e Gratidão")
    st.write("Sua contribuição fortalece a nossa comunidade.")

st.divider()

# --- CORPO PRINCIPAL ---
col_form, col_img = st.columns([1, 1], gap="large")

with col_form:
    st.subheader("Registrar Contribuição")
    with st.form("form_dizimo", clear_on_submit=True):
        nome = st.text_input("Nome Completo")
        cpf = st.text_input("CPF (Apenas números)")
        valor = st.number_input("Valor da Oferta (R$)", min_value=1.0, step=10.0)
        
        metodo = st.radio("Selecione o método:", ["PIX", "Boleto Bancário"])
        
        submit = st.form_submit_button("Gerar Pagamento")
        
        if submit:
            if nome and cpf and valor > 0:
                conn = sqlite3.connect('igreja.db')
                c = conn.cursor()
                data_atual = datetime.now().strftime("%d/%m/%Y %H:%M")
                c.execute("INSERT INTO dizimos (nome, cpf, valor, data) VALUES (?,?,?,?)", 
                          (nome, cpf, valor, data_atual))
                conn.commit()
                conn.close()
                st.success(f"Obrigado, {nome}! Siga para o pagamento abaixo.")
            else:
                st.error("Por favor, preencha todos os campos.")

with col_img:
    # Aqui usamos a imagem que você enviou (substitua pelo link dela após subir ao GitHub)
    st.image("https://raw.githubusercontent.com/SEU_USUARIO/SEU_REPO/main/Copia-de-Noticias-51.jpg", 
             caption="Juntos somos mais fortes", use_container_width=True)

# --- RODAPÉ/PAGAMENTO ---
if 'submit' in locals() and submit:
    st.divider()
    if metodo == "PIX":
        st.info("### 📱 Pagamento via PIX")
        st.code("00020126360014BR.GOV.BCB.PIX0114SUACHAVEAQUI")
        st.write("Abra o app do seu banco e use a opção 'PIX Copia e Cola'.")
    else:
        st.info("### 📄 Pagamento via Boleto")
        st.write("O seu boleto foi gerado. Clique no botão abaixo para baixar.")
        st.button("⬇️ Baixar Boleto")
