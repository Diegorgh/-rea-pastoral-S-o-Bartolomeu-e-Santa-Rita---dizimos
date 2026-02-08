import streamlit as st
import sqlite3
from datetime import datetime

# --- CONFIGURAÇÕES DE ESTILO E DESIGN ---
st.set_page_config(page_title="Dízimo Paroquial", page_icon="⛪", layout="centered")

# Injeção de CSS para o Estilo Litúrgico
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Open+Sans&display=swap');
    
    .main { background-color: #F5F5DC; } /* Bege Litúrgico */
    
    h1, h2, h3 { 
        font-family: 'Playfair Display', serif; 
        color: #000080; /* Azul Marinho */
        text-align: center;
    }
    
    p, label { font-family: 'Open Sans', sans-serif; color: #333; }
    
    .stButton>button {
        background-color: #000080;
        color: white;
        border-radius: 8px;
        border: 1px solid #D4AF37; /* Detalhe Dourado */
        font-weight: bold;
    }
    
    .stButton>button:hover { border: 2px solid #D4AF37; color: #D4AF37; }
    </style>
    """, unsafe_allow_html=True)

# --- LÓGICA DE NAVEGAÇÃO (STEPPER) ---
if 'passo' not in st.session_state:
    st.session_state.passo = 1
if 'dados' not in st.session_state:
    st.session_state.dados = {}

def avancar(): st.session_state.passo += 1
def voltar(): st.session_state.passo -= 1

# --- CONTEÚDO ---

# Header & Hero
st.image("https://raw.githubusercontent.com/SEU_USUARIO/SEU_REPO/main/Copia-de-Noticias-51.jpg", use_container_width=True)
st.title("Sua gratidão sustenta nossa missão")
st.markdown("<p style='text-align: center;'><i>'O dízimo é um gesto de amor e partilha.'</i></p>", unsafe_allow_html=True)

st.divider()

# Módulo de Doação (Checkout em Passos)
container = st.container(border=True)

with container:
    if st.session_state.passo == 1:
        st.subheader("Passo 1: Identificação")
        st.session_state.dados['nome'] = st.text_input("Nome Completo", value=st.session_state.dados.get('nome', ''))
        st.session_state.dados['cpf'] = st.text_input("CPF (para o recibo)", value=st.session_state.dados.get('cpf', ''))
        st.button("Próximo ➔", on_click=avancar)

    elif st.session_state.passo == 2:
        st.subheader("Passo 2: Valor e Periodicidade")
        valor_opcoes = ["R$ 50,00", "R$ 100,00", "R$ 200,00", "Outro"]
        escolha = st.radio("Selecione o valor:", valor_opcoes)
        
        if escolha == "Outro":
            st.session_state.dados['valor'] = st.number_input("Valor customizado", min_value=1.0)
        else:
            st.session_state.dados['valor'] = float(escolha.replace("R$ ", "").replace(",", "."))
            
        st.session_state.dados['recorrente'] = st.checkbox("Desejo que seja um dízimo mensal recorrente")
        
        col1, col2 = st.columns(2)
        col1.button("⬅ Voltar", on_click=voltar)
        col2.button("Próximo ➔", on_click=avancar)

    elif st.session_state.passo == 3:
        st.subheader("Passo 3: Pagamento")
        metodo = st.selectbox("Forma de Pagamento", ["PIX (Recomendado)", "Boleto Bancário"])
        
        st.write(f"**Resumo:** {st.session_state.dados['nome']} - R$ {st.session_state.dados['valor']:.2f}")
        
        if st.button("Finalizar e Gerar Pagamento"):
            st.session_state.passo = 4
            st.rerun()
            
    elif st.session_state.passo == 4:
        st.balloons()
        st.subheader("🙏 Agradecimento")
        st.markdown(f"### Deus ama quem dá com alegria!")
        st.write(f"Obrigado, {st.session_state.dados['nome']}. Seu gesto ajuda nossa paróquia nas dimensões Religiosa, Social e Missionária.")
        st.code("00020126360014BR.GOV.BCB.PIX0114SUACHAVEPIX") # QR Code dinâmico entraria aqui
        st.info("Copia o código PIX acima para finalizar no seu banco.")
        if st.button("Fazer outra contribuição"):
            st.session_state.passo = 1
            st.rerun()

# Rodapé de Transparência
st.divider()
col_a, col_b, col_c = st.columns(3)
col_a.metric("Religiosa", "Culto e Clero")
col_b.metric("Social", "Obras de Caridade")
col_c.metric("Missionária", "Evangelização")
