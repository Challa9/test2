import sqlite3

# created a file
connection = sqlite3.connect("test_users.db")
cursor = connection.cursor()

# created a table called test_users
# connection.execute("CREATE TABLE test_users (name, password)")
# connection.commit()

# asking for name and password inputs
# name_input = input("Name: ")
# password_input = input("Password:")

# inserting data into the table
# connection.execute("INSERT INTO test_users_data VALUES (?, ?)", [name_input, password_input])
# connection.commit()

# recalling the data to use
product_cursor = cursor.execute("SELECT name, password FROM test_users_data")

# turning it into a list
product_list = product_cursor.fetchall()

# printing out the data
for names, passwords in product_list:
    print("Name:{}\nPassword:{}".format(names, passwords))

name_check = cursor.execute("SELECT name FROM test_users_data")
name_list = product_cursor.fetchall()

names_list = []
for names in name_list:
    names_list.append(names)

print("Names list:", names_list)

if "Challa" not in names_list:
    print(True)
