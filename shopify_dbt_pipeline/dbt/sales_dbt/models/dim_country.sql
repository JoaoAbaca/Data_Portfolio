{{ config(materialized='table') }}

SELECT DISTINCT
    country
FROM {{ ref('fact_orders') }}
WHERE country IS NOT NULL
