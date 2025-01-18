# Create your utility functions here, feel free to make additional files
import json
from db.connection import create_conn, close_db, db
from pprint import pprint
from db.data.rides import rides 


def get_parks_data():
    db_run_query = db.run("SELECT * FROM parks;")

    # Column titles -> park_id, park_name, year_opened, annual_attendance 
    column_titles = [db.columns[idx]['name'] for idx in range(len(db.columns))]

    # Rows -> 
    rows = [db_run_query[idx] for idx in range(len(db_run_query))]#

    parks_data = [dict(zip(column_titles, row)) for row in rows]

    return parks_data



def utils_park_names_to_id():
    parks_data = get_parks_data()

    # [1, 2, 3, 4]
    park_ids = [park['park_id'] for park in parks_data]

    # ['Thorpe Park', 'Alton Towers', 'Chessington World of Adventures', 'Tivoli Gardens']
    park_names = [park['park_name'] for park in parks_data]

    map_dict_park_name_to_id = {}

    for idx in range(len(parks_data)):
        park_name = park_names[idx] 
        park_id = park_ids[idx]
        map_dict_park_name_to_id[park_name] = park_id 

    return map_dict_park_name_to_id


def prepare_rides_data():
    utils_name_to_id = utils_park_names_to_id()

    with open('./db/data/rides.py', 'w') as rides_file:

        for idx, ride in enumerate(rides):
            try:
                if rides[idx]['park_name'] in utils_name_to_id.keys():
                    park_name = rides[idx]['park_name']
                    rides[idx]['park_id'] = utils_name_to_id[park_name]
                    del ride['park_name']
            except KeyError as err:
                print("File already has park_id")
                break
        
        
        rides_data = rides.copy()

        rides_file.write("rides = ")
        rides_file.write(json.dumps(rides_data, indent=1))




