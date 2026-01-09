import psycopg2

connection = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="root123",
    host="localhost",
    port="5433"
)

cursor = connection.cursor()

print("Connected to the database successfully.")

# insert_query = '''CREATE TABLE employees (
#    id SERIAL PRIMARY KEY, name VARCHAR(100), department VARCHAR(100), salary NUMERIC)
#   '''
# cursor.execute(insert_query)
# if(cursor.rowcount== -1):
#    print("Table created successfully.")

#insert data into table
#insert_query = '''INSERT INTO employees (name, department, salary)
 #                 VALUES ('John Doe', 'Engineering', 75000.00)'''

#cursor.execute(insert_query)
#connection.commit()
#print("Inserted a new employee record successfully.")

#delete data from table
delete_query = '''DELETE FROM employees WHERE name=%s '''
cursor.execute(delete_query, ('John Doe',))
connection.commit()
print("Deleted employee record successfully.")


# Close cursor and connection
cursor.close()
connection.close()