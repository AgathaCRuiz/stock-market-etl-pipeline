-- import

with source as (
    select
        "date",            
        "Close",           
        "simbolo"          
    from
        {{ source('stockmarket_alce', 'commodities') }}
),

renamed as (
    select
        cast("date" as date) as data,
        "Close" as valor_fechamento,
        "simbolo" as simbolo -- 🌟 Ajustado com aspas e alias explícito
    from
        source
)

select * from renamed