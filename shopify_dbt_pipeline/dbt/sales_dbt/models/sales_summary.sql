{{ config(materialized='table') }}

SELECT
    d.date AS order_date,
    d.year,
    d.month,
    d.month_name,
    d.weekday_name,
    p.product_type,
    c.country,
    g.gateway,
    
    COUNT(DISTINCT f.order_number) AS num_orders,
    SUM(f.quantity) AS total_quantity,
    SUM(f.total_price_usd) AS total_revenue,
    SUM(f.tax) AS total_tax,
    ROUND(SUM(f.total_price_usd)::numeric / COUNT(DISTINCT f.order_number), 2) AS avg_order_value


FROM {{ ref('fact_orders') }} f
LEFT JOIN {{ ref('dim_date') }} d ON f.order_date = d.date
LEFT JOIN {{ ref('dim_product_type') }} p ON f.product_type = p.product_type
LEFT JOIN {{ ref('dim_country') }} c ON f.country = c.country
LEFT JOIN {{ ref('dim_gateway') }} g ON f.gateway = g.gateway

GROUP BY 
    d.date, d.year, d.month, d.month_name, d.weekday_name,
    p.product_type, c.country, g.gateway
