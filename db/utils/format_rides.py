# Create your utility functions here, feel free to make additional files
import json
from db.connection import create_conn, close_db, db
from pprint import pprint
from db.data.rides import rides 


def utils_park_names_to_id():
    db_run_query = db.run("SELECT * FROM parks")

    map_dict_park_name_to_id = {}
   
    # Park columns and rows
    column_titles = [db.columns[idx]['name'] for idx in range(len(db.columns))]
    rows = [db_run_query[idx] for idx in range(len(db_run_query))]


    parks_data = [dict(zip(column_titles, row)) for row in rows]

    park_ids = [park['park_id'] for park in parks_data]
    park_names = [park['park_name'] for park in parks_data]

    # Map to dictionary
    for idx in range(len(parks_data)):
        map_dict_park_name_to_id[park_names[idx]] = park_ids[idx] 

    return map_dict_park_name_to_id

# print(utils_park_names_to_id())


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
                print("File already has an id")
                break
        
        
        rides_data = rides.copy()

        rides_file.write("rides = ")
        rides_file.write(json.dumps(rides_data, indent=1))




