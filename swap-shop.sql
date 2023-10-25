CREATE DATABASE swap_shop;

USE swap_shop;

CREATE TABLE items(
item_name VARCHAR(50)
);

INSERT INTO items (item_name)
VALUES 
('apple'),
('bike'),
('carpet'),
('plant'),
('television'),
('cushion'),
('scooter'),
('chair'),
('rug'),
('trousers');

SELECT * FROM items;
