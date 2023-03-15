SELECT * FROM order_items; # done

SELECT * FROM orders; # done

SELECT * FROM products; # done

SELECT * FROM customers; # done

SELECT * FROM employees;

SELECT * FROM orders o LEFT JOIN customers c ON o.customer_id = c.id LEFT JOIN order_items oi on o.id = oi.order_id LEFT JOIN products p on oi.product_id = p.id;

SELECT 
o.order_date, o.customer_id,
c.first_name, c.last_name, c.rewards_points, c.registration_date,
oi.order_id, oi.product_id, oi.quantity,
p.sku, p.name, p.description, p.unit_price
FROM orders o 
LEFT JOIN customers c ON o.customer_id = c.id 
LEFT JOIN order_items oi on o.id = oi.order_id 
LEFT JOIN products p on oi.product_id = p.id;

SELECT 
o.order_date, o.customer_id,
c.first_name as customer_first_name, c.last_name as customer_last_name, c.rewards_points as customer_rewards_points, c.registration_date as customer_registration_date,
oi.order_id, oi.product_id, oi.quantity as order_item_quantity,
p.sku as product_sku, p.name as product_name, p.description as product_description, p.unit_price as product_unit_price
FROM orders o 
LEFT JOIN customers c ON o.customer_id = c.id 
LEFT JOIN order_items oi on o.id = oi.order_id 
LEFT JOIN products p on oi.product_id = p.id;