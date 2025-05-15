{{ config(materialized='table') }}

SELECT DISTINCT
    city
FROM {{ ref('fact_orders') }}
WHERE city IS NOT NULL
