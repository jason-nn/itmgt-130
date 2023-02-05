CREATE TABLE customer (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    first_name TEXT,
    last_name TEXT,
    mobile_number TEXT,
    email TEXT UNIQUE
);

INSERT INTO customer 
(first_name, last_name, mobile_number, email)
VALUE 
("Juan", "Dela Cruz", "0917 123 4567", "juan.delacruz@gmail.com");

INSERT INTO customer
(first_name, last_name, mobile_number, email)
VALUES
("John", "Doe", "+1 650 513 0514", "john@pasteel.com"),
("Jules", "Dupont", "+33-655-598-001", "jules.dupont@autoclassique.com");

CREATE TABLE product (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    sku TEXT UNIQUE,
    label TEXT,
    brand TEXT,
    category TEXT,
    srp_cents INT
);

INSERT INTO product (sku, label, brand, category, srp_cents) VALUES 
(10001, "Frozen Pizza 13in", "Mario's", "Frozen Food", 35000),
(10002, "Tolgate Pure White 250g", "Tolgate", "Dental Hygiene", 27500),
(10003, "Snowman (Audiophile Edition)", "Azure Microphones", "Electronics", 1200000);

CREATE TABLE product_in_cart (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    customer_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT DEFAULT 1,
    CONSTRAINT `fk_product_in_cart_customer`
        FOREIGN KEY (customer_id) REFERENCES customer (id)
        ON DELETE CASCADE 
        ON UPDATE RESTRICT,
    CONSTRAINT `fk_product_in_cart_product`
        FOREIGN KEY (product_id) REFERENCES product (id)
        ON DELETE CASCADE 
        ON UPDATE RESTRICT
);

INSERT INTO product_in_cart (customer_id, product_id, quantity) VALUES 
(1, 1, 2),
(2, 1, 1),
(2, 1, 2),
(3, 3, 1);