import psycopg2
from psycopg2 import sql, OperationalError

def connect_to_postgres():
    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect(
            dbname="postgres",        # use your actual database name
            user="postgres",          # default superuser
            password="root123",          # replace with your password
            host="localhost",         # or IP if remote
            port="5433"               # default PostgreSQL port
        )
        
        # Create a cursor
        cur = conn.cursor()

        # Execute a query
        cur.execute("SELECT version();")

        # Fetch result
        version = cur.fetchone()
        print("PostgreSQL version:", version[0])

        # Close cursor and connection
        cur.close()
        conn.close()

    except OperationalError as e:
        print("Error connecting to PostgreSQL:", e)

if __name__ == "__main__":
    connect_to_postgres()