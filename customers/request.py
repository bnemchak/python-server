import sqlite3
import json

from models import Customer

customers = [
    Customer(1, 'Hannah Hall', '123 street', 'hh@gmail.com', 'password'),
    Customer(2, 'Brian Neal', '456 street', 'bn@gmail.com', 'password'),
    Customer(3, 'Mitchell Blom', '789 street', 'mb@gmail.com', 'password'),
]

def get_all_customers():
    with sqlite3.connect("./kennel.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.email,
            a.password,
        FROM customer a
        """)

        customers = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            customer = Customer(row['id'], row['name'], row['address'], row['email'], row['password',])

            customers.append(customer.__dict__)

    return json.dumps(customers)

def get_single_customer(id):
    with sqlite3.connect("./kennel.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.email,
            a.password,
        FROM customer a
        WHERE a.id = ?
        """, ( id ))

        data = db_cursor.fetchone()

        customer = Customer(data['id'], data['name'], data['address'], data['email'], data['password',])

        return json.dumps(customer.__dict__)

def create_customer(customer):
    max_id = customers[-1].id

    new_id = max_id + 1

    customer["id"] = new_id
    customers.append(customer)

    return customer

def delete_customer(id):
    customer_index = -1

    for index, customer in enumerate(customers):
        if customer.id == id:
            customer_index = index

    if customer_index >= 0:
        customers.pop(customer_index)

def update_customer(id, new_customer):
    for index, customer in enumerate(customers):
        if customer.id == id:
            customers[index] = new_customer
            break

def get_customers_by_email(email):

    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        from Customer c
        WHERE c.email = ?
        """, ( email, ))

        customers = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            customer = Customer(row['id'], row['name'], row['address'], row['email'] , row['password'])
            customers.append(customer.__dict__)

    return json.dumps(customers)
