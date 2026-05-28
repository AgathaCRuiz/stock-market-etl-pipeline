{% docs __overview__ %}

# 📊 Pipeline de Engenharia de Dados - Mercado de Commodities

Bem-vindo à documentação técnica do nosso ecossistema de dados! Este projeto foi desenvolvido para consolidar dados históricos de fechamento de mercado de commodities com o histórico de movimentações financeiras de compra e venda.

---

### 🏗️ Arquitetura da Solução

O pipeline é dividido em três camadas principais:

1. **Ingestão (Extract & Load):** Scripts em Python localizados na pasta `src/` que extraem os dados de mercado e populam o banco de dados PostgreSQL hospedado no Render.
2. **Transformação & Modelagem (dbt):** Modelos estruturados dentro da pasta `datawarehouse/` que realizam a limpeza (Staging) e a consolidação de regras de negócio no Data Mart (`dm_commodities`).
3. **Visualização (BI):** Um dashboard interativo construído em **Streamlit** (`app/app.py`) focado na análise dos dados consolidados.

---

### 🗂️ Estrutura das Camadas de Dados

- **Sources / Seeds:** Origem dos dados históricos de preços e arquivos estáticos de movimentações.
- **Staging (`stg_...`):** Limpeza inicial, padronização de tipos de dados (como conversão de datas) e renomeação de colunas.
- **Data Mart (`dm_...`):** Camada analítica final onde ocorre o cruzamento de dados (`LEFT JOIN`) e o cálculo de indicadores como volume financeiro e ganho/perda por operação.

---

### 🚀 Como Executar o Projeto

Para rodar as transformações locais e atualizar o Data Warehouse:

```bash
cd datawarehouse
dbt run
```

{% enddocs %}