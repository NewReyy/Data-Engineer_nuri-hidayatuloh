#Membuat Database
CREATE DATABASE alta_online_shop;

#Menggunakan Database
USE alta_online_shop;

#Create table user
CREATE TABLE user (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(255),
    tanggal_lahir DATE,
    status_user VARCHAR(50),
    gender VARCHAR(10),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

#Create table product
CREATE TABLE product (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(255),
    product_type VARCHAR(50),
    product_description TEXT,
    operators VARCHAR(50)
);

#Create table transaction
CREATE TABLE transaction (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    product_id INT,
    FOREIGN KEY (user_id) REFERENCES user(user_id),
    FOREIGN KEY (product_id) REFERENCES product(product_id)
);

#Create table transaction_detail
CREATE TABLE transaction_detail (
    detail_id INT AUTO_INCREMENT PRIMARY KEY,
    transaction_id INT,
    quantity INT,
    price DECIMAL(10,2),
    transaction_date DATE,
    FOREIGN KEY (transaction_id) REFERENCES transaction(transaction_id)
);

#Create table kurir
CREATE TABLE kurir (
    id INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

ALTER TABLE kurir ADD COLUMN ongkos_dasar INT(255) AFTER `name`;

SELECT * FROM kurir;

#Rename table kurir menjadi shipping
RENAME TABLE kurir TO shipping;

#Drop table shipping
DROP TABLE shipping;

#Create table payment_method
CREATE TABLE payment_method (
	payment_id INT PRIMARY KEY,
    payment_name VARCHAR(255)
);

#Create table payment_method_description
CREATE TABLE payment_method_description (
    payment_id INT PRIMARY KEY,
    `description` TEXT,
    FOREIGN KEY (payment_id) REFERENCES payment_method(payment_id)
);

#Create table alamat
CREATE TABLE alamat (
    alamat_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    alamat VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES user(user_id)
);

#Create table user_payment_method_detail (many-to-many)
CREATE TABLE user_payment_method_detail (
    user_id INT,
    payment_id INT,
    PRIMARY KEY (user_id, payment_id),
    FOREIGN KEY (user_id) REFERENCES user(user_id),
    FOREIGN KEY (payment_id) REFERENCES payment_method(payment_id)
);
