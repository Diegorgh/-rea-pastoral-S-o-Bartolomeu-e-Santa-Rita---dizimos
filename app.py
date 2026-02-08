import streamlit as st
import sqlite3
from datetime import datetime

# 1. Configuração da Página
st.set_page_config(page_title="Portal do Dizimista", layout="wide")

# 2. Título e Estilo (Forçado para o Render)
st.markdown("""
    <style>
    .main-title {
        text-align: center;
        color: #1a4a7a;
        font-size: 50px;
        font-weight: bold;
        padding-top: 10px;
    }
    .sub-title {
        text-align: center;
        font-size: 20px;
        color: #555;
        margin-bottom: 30px;
    }
    </style>
    <div class="main-title">⛪ Dízimo e Gratidão</div>
    <div class="sub-title">Sua contribuição fortalece a nossa comunidade.</div>
    """, unsafe_allow_html=True)

st.write("---")

# 3. Layout com Colunas
col_form, col_espaco, col_img = st.columns([1.5, 0.1, 1])

with col_form:
    st.subheader("🙏 Registre sua Oferta")
    with st.form("form_pagamento"):
        nome = st.text_input("Nome Completo")
        cpf = st.text_input("CPF")
        valor = st.number_input("Valor (R$)", min_value=1.0)
        metodo = st.radio("Forma de Pagamento", ["PIX", "Boleto"])
        
        clicou = st.form_submit_button("Gerar Pagamento")

with col_img:
    # LINK DA IMAGEM: Use o link que termina em .jpg do seu GitHub
    # Exemplo: https://raw.githubusercontent.com/USUARIO/REPO/main/Copia-de-Noticias-51.jpg
    url_foto = "COLE_AQUI_O_SEU_LINK_RAW_DO_GITHUB"
    
    try:
        st.image(url_foto, caption="Juntos somos mais fortes", use_container_width=True)
    except:
        st.error("Erro ao carregar imagem. Verifique o link no código.")

# 4. Ação após o clique
if clicou:
    if nome and cpf:
        st.success(f"Obrigado, {nome}!")
        if metodo == "PIX":
            st.info("### 📱 Copia e Cola o PIX")
            st.code("00020126360014BR.GOV.BCB.PIX0114SUACHAVE")
if __name__ == "__main__":
    init_db()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
