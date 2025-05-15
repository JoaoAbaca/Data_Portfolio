{{ config(materialized='table') }}

SELECT DISTINCT
    product_type
FROM {{ ref('fact_orders') }}
WHERE product_type IS NOT NULL
