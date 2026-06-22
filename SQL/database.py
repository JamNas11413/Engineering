import sqlite3

connection = sqlite3.connect('database.db')  # to connect to datbase
cursor = connection.cursor() # to interct with db using sql cammond

# tables
cammond1 = '''CREATE TABLE IF NOT EXISTS store(
        store_id INTEGER PRIMARY KEY, location TEXT NOT NULL
    )'''

cursor.execute(cammond1)

cammond2 = '''CREATE TABLE IF NOT EXISTS purchases(
        purchases_id INTEGER PRIMARY KEY, location TEXT NOT NULL
    )'''
cursor.execute(cammond2)

# insert info

cursor.execute("""
select * from purchases 
""")

connection.commit() 

connection.close()

result = cursor.fetchall()

print(result)