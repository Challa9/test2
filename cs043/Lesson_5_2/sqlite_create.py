import sqlite3

import sqlite3

connection = sqlite3.connect('test.db')

# creating the test_product table
# connection.execute("CREATE TABLE test_products (name, price, weight)")

# inserting values into test_product table
# connection.execute("INSERT INTO test_products VALUES (?, ?, ?)", ["book", 7.99, 0.5])

'''
connection.execute('INSERT INTO products VALUES (?, ?, ?)', ['book', 7.99, 0.5])
connection.execute('INSERT INTO products VALUES (?, ?, ?)', ['drink', 2.00, 0.4])
connection.execute('INSERT INTO products VALUES (?, ?, ?)', ['car', 70000, 1875])
'''
# connection.execute('INSERT INTO test_products VALUES (?, ?, ?)', ['drink', 2.00, 0.4])
# connection.execute('INSERT INTO test_products VALUES (?, ?, ?)', ['car', 70000, 1875])
# saving the data into the table before closing
connection.commit()

# cursor is keeps track of returend rows
cursor = connection.cursor()

# selects what you want from the cursor table
product_cursor = cursor.execute('SELECT name, weight FROM test_products')

# fetchall method converts the set of rows in the cursor to a python list
product_list = product_cursor.fetchall()

for name, weights in product_list:
    print("Product: {}, Weight: {}".format(name, weights))

# Updating the table here; changes everything
connection.execute("UPDATE test_products SET weight = ?", [9])
connection.commit()

connection.execute("DELETE FROM test_products")
connection.commit()

# the deletes everything from test_products if price is greater than 100
# connection.execute("DELETE FROM test_products WHERE price > ?", [100])
