-- # How many customers are in the database? 
SELECT COUNT(id) FROM customers;

SELECT * FROM order_items;

SELECT * FROM orders;

SELECT * FROM products;

SELECT id FROM products WHERE sku = 'AMERICANO';

-- # How many orders involved the "AMERICANO" SKU?
SELECT COUNT(order_id) FROM order_items WHERE product_id = 1;

SELECT oi.order_id, oi.quantity, p.unit_price, oi.quantity * p.unit_price FROM order_items oi LEFT JOIN products p on oi.product_id = p.id;

-- # Get the total sale value of each order.
SELECT order_id, SUM(oi.quantity * p.unit_price) FROM order_items oi LEFT JOIN products p on oi.product_id = p.id GROUP BY oi.order_id;

SELECT o.order_date, oi.quantity, p.unit_price FROM order_items oi LEFT JOIN orders o on oi.order_id = o.id LEFT JOIN products p on oi.product_id = p.id;

-- # Get the total sale value of each day.
SELECT o.order_date, SUM(oi.quantity * p.unit_price) FROM order_items oi LEFT JOIN orders o on oi.order_id = o.id LEFT JOIN products p on oi.product_id = p.id GROUP BY o.order_date;
