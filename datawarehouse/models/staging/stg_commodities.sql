-- import

with source as (
    select
        "date",            -- Totalmente minúsculo
        "Close",           -- Com o C maiúsculo conforme o banco pediu
        "simbolo"          -- Totalmente minúsculo
    from
        {{ source('stockmarket_alce', 'commodities') }}
),

renamed as (
    select
        cast("date" as date) as data,
        "Close" as valor_fechamento,
        simbolo
    from
        source
)

select * from renamed