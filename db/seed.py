# You will need to write your database connection file before being able to run your seed file

from db.connection import db
from db.data.parks import parks
from db.data.rides import rides
from db.utils.format_rides import prepare_rides_data


def seed(db, parks, rides, stalls, foods):
    '''Seeds database'''
    db.run("DROP TABLE IF EXISTS rides;")
    db.run("DROP TABLE IF EXISTS stalls;")
    db.run("DROP TABLE IF EXISTS foods;")
    db.run("DROP TABLE IF EXISTS stalls_foods;")
    db.run("DROP TABLE IF EXISTS parks;")
    create_parks()
    create_rides()
    populate_table("parks", parks)
    prepare_rides_data()
    populate_table("rides", rides)

# The order in which we create our tables is important. First, let's create tables that do not reference other tables.

# TABLE parks 
def create_parks():
    return db.run("""
        CREATE TABLE IF NOT EXISTS parks (
        park_id SERIAL PRIMARY KEY,
        park_name VARCHAR NOT NULL,
        year_opened INTEGER NOT NULL,
        annual_attendance INTEGER NOT NULL
        )
    """)


def create_rides():
    '''Create your rides table in the query below'''

    return db.run("""
        CREATE TABLE IF NOT EXISTS rides (
            ride_id SERIAL PRIMARY KEY,
            park_id INT NOT NULL REFERENCES parks(park_id),
            ride_name VARCHAR NOT NULL,
            year_opened INTEGER NOT NULL,
            votes INTEGER NOT NULL
        )
    """)


def populate_table(table_name, table_data ):

    db.run(f"SELECT * FROM {table_name}")

    # Ignore ID column
    ignore_id_col = f"{table_name[:-1]}_id"
 
    # Columns 
    table_columns = [f"{db.columns[idx]['name']}" for idx in range(len(db.columns)) if ignore_id_col != db.columns[idx]['name']]
    table_columns = ", ".join(table_columns)

    # Placeholder columns
    table_columns_placeholders = [f":{db.columns[idx]['name']}_" for idx in range(len(db.columns)) if ignore_id_col != db.columns[idx]['name']]

    # Arguments + Placeholders
    args = {}
    placeholders = []

    for i, row in enumerate(table_data):
        placeholder_row = [f"{placeholder}{i + 1}" for placeholder in table_columns_placeholders]
        placeholders.append(f"({", ".join(placeholder_row)})")
        
        for key, value in row.items():
            args[f"{key}_{i + 1}"] = f"{value}"

    # Query start...
    insert_query = f"INSERT INTO {table_name} ({table_columns}) VALUES "
    insert_query += ", ".join(placeholders)

    # Run query
    return db.run(insert_query, **args)



# Populate the tables
seed(db, parks, rides, None, None)