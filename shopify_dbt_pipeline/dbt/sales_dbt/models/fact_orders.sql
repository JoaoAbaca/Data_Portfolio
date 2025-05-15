{{ config(materialized='table') }}

SELECT
    order_number,
    customer_id,
    invoice_date::date AS order_date,
    product_id,
    product_type,
    variant_id,
    country,
    city,
    gateway,
    quantity,
    subtotal,
    total_price_usd,
    tax
FROM {{ ref('stg_orders') }}
