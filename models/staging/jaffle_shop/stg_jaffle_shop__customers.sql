with 

source as (

    select * from {{ source('default', 'jaffle_shop_customers') }}

),

renamed as (

    select
        id,
        first_name,
        last_name

    from source

)

select * from renamed