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
insert_query = '''SELECT * FROM employees'''
cursor.execute(insert_query)
records = cursor.fetchall()
for rows in records:
    print(rows)
print(records)
connection.commit()
# print("Inserted a new employee record successfully.")

# Close cursor and connection
cursor.close()
connection.close()
