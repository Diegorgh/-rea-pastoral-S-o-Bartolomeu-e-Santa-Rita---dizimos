import streamlit as st
import sqlite3
from datetime import datetime

# 1. Configuração da Página
st.set_page_config(page_title="Portal do Dizimista", layout="wide")

# 2. Estilo CSS para garantir que o Título apareça
st.markdown("""
    <style>
    .titulo-igreja {
        text-align: center;
        color: #1a4a7a;
        font-size: 40px;
        font-weight: bold;
        padding: 20px;
        background-color: #ffffff;
        border-radius: 15px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
    }
    </style>
    <div class="titulo-igreja">⛪ Área Pastoral São Bartolomeu e Santa Rita</div>
    <p style='text-align: center; font-size: 18px;'>Dízimo: Uma oferta de amor e gratidão.</p>
    """, unsafe_allow_html=True)

st.write("---")

# 3. Layout com Colunas (Formulário à esquerda, Imagem à direita)
col_form, col_espaco, col_img = st.columns([1.5, 0.1, 1])

with col_form:
    st.subheader("🙏 Registre sua Contribuição")
    with st.form("form_dizimo", clear_on_submit=True):
        nome = st.text_input("Nome Completo")
        cpf = st.text_input("CPF")
        valor = st.number_input("Valor (R$)", min_value=1.0, step=10.0)
        metodo = st.radio("Forma de Pagamento", ["PIX", "Boleto"])
        
        botao = st.form_submit_button("Gerar Pagamento")

with col_img:
    # Este é o link público que o Render consegue ver:
    url_foto = "https://raw.githubusercontent.com/Diegorgh/-rea-pastoral-S-o-Bartolomeu-e-Santa-Rita---dizimos/main/Copia-de-Noticias-51.jpg"
    
    try:
        st.image(url_foto, use_container_width=True)
    except:
        st.error("Não foi possível carregar a imagem do GitHub.")
    
# 4. Ação após o clique no botão
if botao:
    if nome and cpf:
        st.balloons()
        st.success(f"Obrigado por sua fidelidade, {nome}!")
        if metodo == "PIX":
            st.info("### 📱 PIX Copia e Cola")
            st.code("00020126360014BR.GOV.BCB.PIX0114SUACHAVEAQUI")
            st.write("Use o app do seu banco para pagar.")
    else:
        st.error("Por favor, preencha o Nome e o CPF para continuar.")
