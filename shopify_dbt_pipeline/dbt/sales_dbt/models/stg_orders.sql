{{ config(materialized='view') }}

SELECT
    "Order Number" AS order_number,
    "Customer Id" AS customer_id,
    "Invoice Date" AS invoice_date,
    "Product Id" AS product_id,
    "Quantity" AS quantity,
    "Subtotal Price" AS subtotal,
    "Total Price Usd" AS total_price_usd,
    "Total Tax" AS tax,
    "Billing Address Country" AS country,
    "CITY" AS city,
    "Product Type" AS product_type,
    "Variant Id" AS variant_id,
    "Gateway" AS gateway
FROM {{ source('public', 'raw_orders') }}
