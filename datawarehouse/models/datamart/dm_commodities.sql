with staging_commodities as (
    select 
        data,
        simbolo,
        valor_fechamento
    from {{ ref('stg_commodities') }}
),

staging_movimentacao as (
    select 
        data,
        simbolo,
        acao,
        quantidade
    from {{ ref('stg_movimentacao_commodities') }}
)

select
    m.data,
    m.simbolo,
    c.valor_fechamento,
    m.acao,
    m.quantidade,
    (m.quantidade * c.valor_fechamento) as valor,
    case
        when m.acao = 'sell' then (m.quantidade * c.valor_fechamento)
        else -(m.quantidade * c.valor_fechamento)
    end as ganho
from staging_movimentacao m
left join staging_commodities c  -- 🌟 Alterado de INNER para LEFT JOIN
    on m.data = c.data 
    and m.simbolo = c.simbolo