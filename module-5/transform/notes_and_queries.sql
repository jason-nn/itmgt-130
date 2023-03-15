-- start by looking at all tables to determine how to join and which tables are relevant 

SELECT * FROM order_items;

SELECT * FROM orders;

SELECT * FROM products;

SELECT * FROM customers;

SELECT * FROM employees;

-- employees is not connected to other tables, but will join other tables starting with orders as the base table
-- join with customers table on customer id
-- join with order items on order id
-- join with products on product id 

SELECT * 
FROM orders o 
LEFT JOIN customers c ON o.customer_id = c.id 
LEFT JOIN order_items oi on o.id = oi.order_id 
LEFT JOIN products p on oi.product_id = p.id;

-- remove "id" columns as they are unclear in the big table and appear multiple times which may be confusing

SELECT 
o.order_date, o.customer_id,
c.first_name, c.last_name, c.rewards_points, c.registration_date,
oi.order_id, oi.product_id, oi.quantity,
p.sku, p.name, p.description, p.unit_price
FROM orders o 
LEFT JOIN customers c ON o.customer_id = c.id 
LEFT JOIN order_items oi on o.id = oi.order_id 
LEFT JOIN products p on oi.product_id = p.id;

-- rename columns to be more explicit for ease of parsing as something like name on product could be confused with customer name

SELECT 
o.order_date, o.customer_id,
c.first_name as customer_first_name, c.last_name as customer_last_name, c.rewards_points as customer_rewards_points, c.registration_date as customer_registration_date,
oi.order_id, oi.product_id, oi.quantity as order_item_quantity,
p.sku as product_sku, p.name as product_name, p.description as product_description, p.unit_price as product_unit_price
FROM orders o 
LEFT JOIN customers c ON o.customer_id = c.id 
LEFT JOIN order_items oi on o.id = oi.order_id 
LEFT JOIN products p on oi.product_id = p.id;