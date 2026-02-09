import streamlit as st
import sqlite3
from datetime import datetime

st.set_page_config(page_title="Portal do Dizimista", layout="wide")

# Conexão simples para salvar os dados
def salvar_dados(nome, cpf, valor):
    conn = sqlite3.connect('igreja.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS dizimos 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, cpf TEXT, valor REAL, data TEXT)''')
    data_hoje = datetime.now().strftime("%d/%m/%Y %H:%M")
    c.execute("INSERT INTO dizimos (nome, cpf, valor, data) VALUES (?,?,?,?)", (nome, cpf, valor, data_hoje))
    conn.commit()
    conn.close()

# Layout Profissional
st.markdown("<h1 style='text-align: center; color: #1a4a7a;'>⛪ Área Pastoral São Bartolomeu e Santa Rita</h1>", unsafe_allow_html=True)

col_form, col_img = st.columns([1.5, 1])

with col_form:
    st.subheader("🙏 Registre sua Oferta")
    with st.form("form_dizimo", clear_on_submit=True):
        nome = st.text_input("Nome Completo")
        cpf = st.text_input("CPF")
        valor = st.number_input("Valor (R$)", min_value=1.0)
        submit = st.form_submit_button("Gerar Pagamento PIX")
        
        if submit and nome and cpf:
            salvar_dados(nome, cpf, valor)
            st.success(f"Obrigado, {nome}! Deus abençoe.")
            st.info("📱 PIX Copia e Cola: `00020126360014BR.GOV.BCB.PIX0114SUACHAVEAQUI`")

with col_img:
    url_foto = "https://raw.githubusercontent.com/Diegorgh/-rea-pastoral-S-o-Bartolomeu-e-Santa-Rita---dizimos/main/Copia-de-Noticias-51.jpg"
    st.image(url_foto, use_container_width=True)
