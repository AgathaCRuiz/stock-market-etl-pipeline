{% docs contribuicao_e_models %}

## Contribuição

### Descrição dos Models

#### dm_commodities.sql
Este modelo de Data Mart (`dm_commodities`) realiza a junção dos dados tratados de preços históricos de commodities com as tabelas de movimentações e transações financeiras. O objetivo principal é consolidar indicadores consolidados de posição, valores de fecho e volumetria de compras e vendas por símbolo.

##### Principais transformações:
- Cruzamento das tabelas de staging usando chaves de data e símbolo.
- Cálculo de métricas acumuladas de quantidade movimentada.
- Renomeação e tipagem final para consumo em ferramentas de BI.

{% enddocs %}