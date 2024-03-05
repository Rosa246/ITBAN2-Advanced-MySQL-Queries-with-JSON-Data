import pymysql
from faker import Faker
import random

# Connect to MySQL database
db = pymysql.connect(host='localhost', user='root', password='', database='ecommerce')
cursor = db.cursor()

fake = Faker()

# Function to get order IDs from the orders table
def get_order_ids():
    cursor.execute("SELECT order_id FROM orders")
    order_ids = [row[0] for row in cursor.fetchall()]
    return order_ids

# Function to get product IDs from the products table
def get_product_ids():
    cursor.execute("SELECT product_id FROM products")
    product_ids = [row[0] for row in cursor.fetchall()]
    return product_ids

# Generate and insert data into order_details table
def insert_order_details(num_records):
    order_ids = get_order_ids()
    product_ids = get_product_ids()
    for _ in range(num_records):
        order_id = random.choice(order_ids)
        product_id = random.choice(product_ids)
        quantity = random.randint(1, 10)
        price = round(random.uniform(10, 100), 2)
        
        sql = "INSERT INTO order_details (order_id, product_id, quantity, price) VALUES (%s, %s, %s, %s)"
        values = (order_id, product_id, quantity, price)
        
        cursor.execute(sql, values)
    
    # Commit changes to the database
    db.commit()

# Define the number of records to insert
num_records_to_insert = 100  # You can change this number as per your requirement

# Call the function to insert data
insert_order_details(num_records_to_insert)

# Close the database connection
db.close()
