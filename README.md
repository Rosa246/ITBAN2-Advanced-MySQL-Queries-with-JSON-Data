## ITBAN2-Advanced-MySQL-Queries-with-JSON-Data
ADVANCE MYSQL QUERIES WITH JSON DATA

SUBMITTED BY:* GANIBE,DHANNICA SHELLY C. & TAGUD ,ROSALLIE L. *
*BSIT3A *
        

1.	Retrieve Product Information

1.1	Write a query to fetch the names and descriptions of all products. 

***sql
SELECT name, description
FROM products;

![image](https://github.com/Rosa246/ITBAN2-Advanced-MySQL-Queries-with-JSON-Data/assets/148986144/cf86147a-8f04-4b7c-b2a8-3c0439a41373)

1.2	Extend the previous query to include specific attributes such as color, size, and price.

***sql
SELECT name, description,
       JSON_EXTRACT(attributes, '$.color') AS color,
       JSON_EXTRACT(attributes, '$.size') AS size,
       JSON_EXTRACT(attributes, '$.price') AS price,
JSON_EXTRACT(attributes, '$.brandName') AS brand
FROM products;

![image](https://github.com/Rosa246/ITBAN2-Advanced-MySQL-Queries-with-JSON-Data/assets/148986144/302b1089-f869-457f-a992-9ad1a1f4a626)

2. Query Orders and Order details

	2.1 Retrieve the details of all orders placed, including the order date, customer ID, 
Product name, quantity, and price.
***sql
SELECT
    o.order_id,
    o.order_date,
    o.customer_id,
    p.name AS product_name,
    od.quantity,
    od.price
FROM
    orders o JOIN
    order_details od ON o.order_id = od.order_id
JOIN products p ON od.product_id = p.product_id;
![image](https://github.com/Rosa246/ITBAN2-Advanced-MySQL-Queries-with-JSON-Data/assets/148986144/439c8d6f-87b8-4e6b-a1a0-a636406e6b60)

2.2 Calculate the total cost of each order.
***sql
SELECT
    o.order_id,
    SUM(od.quantity * od.price) AS total_cost
FROM
    orders o
JOIN
    order_details od ON o.order_id = od.order_id
GROUP BY
    o.order_id;
    ***
![image](https://github.com/Rosa246/ITBAN2-Advanced-MySQL-Queries-with-JSON-Data/assets/148986144/37a098a7-9416-4063-8a0c-3bf00dc0b51f)

3. Filtering Products Based on Attributes
	3.1 Write a query to find all products with a price greater than $50. 

***sql
SELECT *
FROM products
WHERE JSON_EXTRACT(attributes, '$.price') > 50;
***

![image](https://github.com/Rosa246/ITBAN2-Advanced-MySQL-Queries-with-JSON-Data/assets/148986144/7b3fe78e-9ec9-487d-bdc0-0dd43c4021ba)

3.2 Filter products by color and brand, and display their names and prices. 

***sql
SELECT name, JSON_EXTRACT(attributes, '$.price') AS price
FROM products
WHERE JSON_EXTRACT(attributes, '$.color') = 'violet' 
AND JSON_EXTRACT(attributes, '$.brand') = 'Torres-Collins';
***

![image](https://github.com/Rosa246/ITBAN2-Advanced-MySQL-Queries-with-JSON-Data/assets/148986144/d0bae8d4-8d66-4079-8403-2f0a9d5397c3)

4. Calculating Aggregate Data
	4.1 Calculate the total sales revenue generated by each product.

***sql
SELECT 
    p.product_id,
    p.name AS product_name,
    SUM(od.quantity * od.price) AS total_revenue
FROM 
    products p
JOIN 
    order_details od ON p.product_id = od.product_id
GROUP BY 
    p.product_id, p.name;
    ***
![image](https://github.com/Rosa246/ITBAN2-Advanced-MySQL-Queries-with-JSON-Data/assets/148986144/f102524e-65ab-4b11-8889-1e1eb64d11cf)

4.2 Determine the total quantity of each product ordered.

***sql
SELECT 
    p.product_id,
    p.name AS product_name,
    SUM(od.quantity) AS total_quantity
FROM 
    products p
JOIN 
    order_details od ON p.product_id = od.product_id
GROUP BY 
    p.product_id, p.name;
    ***
![image](https://github.com/Rosa246/ITBAN2-Advanced-MySQL-Queries-with-JSON-Data/assets/148986144/c29df690-2e86-47bb-8827-ba8c0092ecc5)

5. Advanced Filtering and Aggregation:
	5.1 Find the top 5 best-selling products based on total quantity sold.
   
***sql
   SELECT
    p.product_id,
    p.name AS product_name,
    SUM(od.quantity) AS total_quantity_sold
FROM
    products p
JOIN
    order_details od ON p.product_id = od.product_id
GROUP BY
    p.product_id, p.name
ORDER BY
    total_quantity_sold DESC Limit 5;
   ***
![image](https://github.com/Rosa246/ITBAN2-Advanced-MySQL-Queries-with-JSON-Data/assets/148986144/d030a07f-96c7-45e2-b574-137606be01c2)

5.2  Identify the average price of products from a specific brand.
***sql
SELECT
    AVG(JSON_EXTRACT(attributes, '$.price')) AS average_price,
    JSON_EXTRACT(attributes, '$.brand') AS brand
FROM
    products
WHERE
    JSON_EXTRACT(attributes, '$.brand') = 'Torres-Collins'
GROUP BY
    JSON_EXTRACT(attributes, '$.brand');
 ***
![image](https://github.com/Rosa246/ITBAN2-Advanced-MySQL-Queries-with-JSON-Data/assets/148986144/fe9a80a5-bc2d-46b3-8ea9-0c531d365b0d)
6. Nested JSON Queries:
	6.1 Retrieve the color and size of a specific product.
***sql
SELECT
    JSON_EXTRACT(attributes, '$.color') AS color,
    JSON_EXTRACT(attributes, '$.size') AS size
FROM
    products
WHERE
    product_id = 1234;
   *** 
![image](https://github.com/Rosa246/ITBAN2-Advanced-MySQL-Queries-with-JSON-Data/assets/148986144/b844fda8-f031-4510-aa1e-d7f2c77ba5f7)


6.2 Extract and display all available attributes of products in JSON format.
***sql
SELECT JSON_OBJECT(
    'product_id', product_id,
    'name', name,
    'description', description,
    'attributes', attributes
) AS product_info
FROM products;
***
![image](https://github.com/Rosa246/ITBAN2-Advanced-MySQL-Queries-with-JSON-Data/assets/148986144/61509430-4c54-47c6-97b8-823604136934)


7. Joining Multiple Tables
	7.1 Write a query to find all orders placed by customers along with the products ordered and 	their quantities.
***sql
SELECT 
    o.order_id,
    o.order_date,
    c.customer_id,
    p.name AS product_name,
    od.quantity
FROM 
    orders o
JOIN 
    order_details od ON o.order_id = od.order_id
JOIN 
    products p ON od.product_id = p.product_id
JOIN 
    customers c ON o.customer_id = c.customer_id;
   ***
![image](https://github.com/Rosa246/ITBAN2-Advanced-MySQL-Queries-with-JSON-Data/assets/148986144/5c470624-a3f7-4c8c-a657-57862a50dbe5)

7.2 Calculate the total revenue generated by each customer.
***sql
SELECT
    CONCAT(c.firstname, ' ', COALESCE(c.middlename, ''), ' ', c.lastname) AS full_name,
    c.customer_id,
    SUM(od.quantity * JSON_EXTRACT(p.attributes, '$.price')) AS total_revenue
FROM
    customers c
JOIN
    orders o ON c.customer_id = o.customer_id
JOIN
    order_details od ON o.order_id = od.order_id
JOIN
    products p ON od.product_id = p.product_id
GROUP BY
    c.customer_id, full_name;
    ***
![image](https://github.com/Rosa246/ITBAN2-Advanced-MySQL-Queries-with-JSON-Data/assets/148986144/b8c9a757-81a2-4b19-b7f8-b52f4a3e461f)

8. Data Manipulation with JSON Functions
	8.1 Update the price of a specific product stored as JSON attribute.
***sql
UPDATE products
SET attributes = JSON_SET(attributes, '$.price', 800.00)
WHERE product_id = 246;
***
![image](https://github.com/Rosa246/ITBAN2-Advanced-MySQL-Queries-with-JSON-Data/assets/148986144/c667c41a-d2b1-4e46-bc9c-a5bc531f8d32)

8.2   Add a new attribute to all products with a default value.
***sql
ALTER TABLE products ADD COLUMN weight VARCHAR(255) DEFAULT 'default_value';
***
![image](https://github.com/Rosa246/ITBAN2-Advanced-MySQL-Queries-with-JSON-Data/assets/148986144/f4600572-e082-4adf-acd5-0b1f53416b32)

9. Advanced JSON Operations
	9.1 Find products with specific attributes that match a given criteria using JSON path expressions.
***sql
   SELECT *
FROM products
WHERE JSON_EXTRACT(attributes, '$.color') = 'Teal'
  AND JSON_EXTRACT(attributes, '$.size') = 'medium';
***
![image](https://github.com/Rosa246/ITBAN2-Advanced-MySQL-Queries-with-JSON-Data/assets/148986144/64a7345a-8df3-4fff-81cf-a451254117b8)

9.2 Extract and display the first element of an array stored within a JSON attribute.
***sql
SELECT JSON_UNQUOTE(JSON_EXTRACT(attributes,'$.color')) 
AS first_element FROM `products`;
***
![image](https://github.com/Rosa246/ITBAN2-Advanced-MySQL-Queries-with-JSON-Data/assets/148986144/b054c126-c094-4013-9be1-db503f9be5e1)



