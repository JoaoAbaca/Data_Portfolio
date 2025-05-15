{{ config(materialized='table') }}

WITH dates AS (
    SELECT DISTINCT order_date AS date
    FROM {{ ref('fact_orders') }}
)

SELECT
    date,
    EXTRACT(year FROM date) AS year,
    EXTRACT(month FROM date) AS month,
    EXTRACT(day FROM date) AS day,
    TO_CHAR(date, 'Month') AS month_name,
    TO_CHAR(date, 'Dy') AS weekday_name,
    EXTRACT(dow FROM date) AS weekday_num
FROM dates
