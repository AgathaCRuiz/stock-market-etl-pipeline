# import
from sqlalchemy import create_engine
import yfinance as yf
import pandas as pd
from dotenv import load_dotenv
import os

# carregar .env
load_dotenv()

# lista de commodities
commodities = ['GC=F', 'SI=F', 'CL=F']

# variáveis ambiente
DB_HOST = os.getenv('DB_HOST_PROD')
DB_PORT = os.getenv('DB_PORT_PROD')
DB_NAME = os.getenv('DB_NAME_PROD')
DB_USER = os.getenv('DB_USER_PROD')
DB_PASS = os.getenv('DB_PASS_PROD')
DB_SCHEMA = os.getenv('DB_SCHEMA_PROD')

# conexão
DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)


# função para buscar dados de uma commodity
def buscar_dados_commodities(simbolo, periodo='5d', intervalo='1d'):

    ticker = yf.Ticker(simbolo)

    dados = ticker.history(
        period=periodo,
        interval=intervalo
    )[['Close']]

    dados['simbolo'] = simbolo

    return dados


# função para buscar todas commodities
def buscar_todas_commodities(lista_commodities):

    todos_dados = []

    for simbolo in lista_commodities:

        dados = buscar_dados_commodities(simbolo)

        todos_dados.append(dados)

    return pd.concat(todos_dados)


# salvar no postgres
def salvar_no_postgres(df, schema='public'):

    df.to_sql(
        'commodities',
        engine,
        if_exists='replace',
        index=True,
        index_label='date',
        schema=schema
    )


# execução principal
if __name__ == "__main__":

    dados_concatenados = buscar_todas_commodities(commodities)

    print(dados_concatenados)

    salvar_no_postgres(
        dados_concatenados,
        schema='public'
    )

    print("Dados salvos no PostgreSQL com sucesso!")