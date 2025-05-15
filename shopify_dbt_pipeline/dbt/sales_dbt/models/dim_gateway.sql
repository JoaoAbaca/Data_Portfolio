{{ config(materialized='table') }}

SELECT DISTINCT
    gateway
FROM {{ ref('fact_orders') }}
WHERE gateway IS NOT NULL
