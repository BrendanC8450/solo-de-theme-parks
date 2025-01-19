import os
from dotenv import load_dotenv
from pg8000.native import Connection

# Load environment variables
load_dotenv()

# Create your create_conn function to return a database connection object

def create_conn():
    db = Connection(
        os.environ['PGUSER'],
        password=os.environ['PGPASSWORD'],
        database=os.environ['PGDATABASE']
    )

    return db

# Variable for connection to db - passed to other files that require it
db = create_conn()

# Create a close_db function that closes a passed database connection object

def close_db(db):
   return db.close()



