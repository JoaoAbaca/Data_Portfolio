-- Product summary by category
SELECT category, COUNT(*) as total_products, AVG(price) as avg_price
FROM products
GROUP BY category
ORDER BY avg_price DESC;

-- Most expensive product
SELECT title, price
FROM products
ORDER BY price DESC;

-- Products with more than 100 reviews
SELECT title, price, count
FROM products
WHERE count > 100
ORDER BY count DESC;

-- Category with the largest number of products
SELECT category, COUNT(*) as total_products
FROM products
GROUP BY category
ORDER BY total_products DESC;

-- Products in a range of prices
SELECT title, price
FROM products
WHERE price BETWEEN 10 AND 50;

-- Top 5 most expensive products by category
SELECT category, title, price
FROM products
WHERE price IN (
    SELECT MAX(price)
    FROM products
    GROUP BY category
)
ORDER BY category;
