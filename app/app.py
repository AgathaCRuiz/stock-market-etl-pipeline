import pandas as pd
import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.exc import ProgrammingError
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Obter as variáveis do arquivo .env
DB_HOST = os.getenv('DB_HOST_PROD')
DB_PORT = os.getenv('DB_PORT_PROD')
DB_NAME = os.getenv('DB_NAME_PROD')
DB_USER = os.getenv('DB_USER_PROD')
DB_PASS = os.getenv('DB_PASS_PROD')
DB_SCHEMA = os.getenv('DB_SCHEMA_PROD')

# Criar a URL de conexão do banco de dados
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Criar o engine de conexão com o banco de dados
engine = create_engine(DATABASE_URL)

def get_data():
    query = f"""
    SELECT
        data,
        simbolo,
        valor_fechamento,
        acao,
        quantidade,  -- 🌟 Tem que ser exatamente como está no DBeaver!
        valor,
        ganho
    FROM
        public.dm_commodities;
    """
    df = pd.read_sql(query, engine)
    return df

# ---------------------------------------------------------
# Interface do Streamlit
# ---------------------------------------------------------

# Configurar a página do Streamlit (Deve ser sempre o primeiro comando do st)
st.set_page_config(page_title='Dashboard de Commodities', layout='wide')

# Título principal do Dashboard
st.title("📊 Dashboard de Commodities")

# Descrição
st.write("""
Este dashboard mostra os dados de commodities e suas transações.
""")

# Obter os dados do banco através da função
df = get_data()

# 💡 MELHORIA: Mostra os dados tratados em uma tabela bonita e interativa no Streamlit
st.subheader("📋 Dados Consolidados (Data Mart)")
st.dataframe(df, use_container_width=True)