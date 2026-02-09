import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(page_title="Painel Admin", layout="wide")

st.title("📊 Painel de Controle Administrativo")

# Sistema de Senha simples
senha = st.text_input("Insira a senha mestra para visualizar os dados", type="password")

if senha == "admin123":
    conn = sqlite3.connect('igreja.db')
    try:
        df = pd.read_sql_query("SELECT * FROM dizimos", conn)
        
        if not df.empty:
            total = df['valor'].sum()
            st.metric("Total Acumulado", f"R$ {total:.2f}")
            
            st.write("### Lista de Contribuições")
            st.dataframe(df, use_container_width=True)
            
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("📥 Baixar Excel (CSV)", csv, "relatorio.csv", "text/csv")
        else:
            st.info("Nenhum dado registrado ainda.")
    except:
        st.warning("O banco de dados ainda está vazio.")
    finally:
        conn.close()
else:
    if senha != "":
        st.error("Senha incorreta!")
