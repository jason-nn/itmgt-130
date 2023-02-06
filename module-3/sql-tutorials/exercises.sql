-- Show the entire `customer` table
select * from simple_ecommerce.customer

-- Show products that are cheaper than 50,000 cents
select * from simple_ecommerce.product p 
where p.srp_cents < 50000

-- Show customer emails beside their products in their cart
select pic.*, c.email from 
simple_ecommerce.product_in_cart pic inner join simple_ecommerce.customer c 
on pic.customer_id = c.id

-- Show the total quantity of each product sold
select product_id, SUM(quantity)
from simple_ecommerce.product_in_cart pic 
group by product_id

-- Show the total sale value of each product sold
select pic.product_id, SUM(pic.quantity * p.srp_cents) as sale_value from 
simple_ecommerce.product_in_cart pic inner join simple_ecommerce.product p 
on pic.product_id = p.id
group by pic.product_id