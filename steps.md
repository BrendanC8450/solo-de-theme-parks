### 1 - Imports 

```bash
pip install pytest pytest-dotenv pg8000
```

### 2 - Run the file

```bash
psql -f ./db/theme-parks.sql
```

Some helpful psql commands:

\c my_database - connect to the desired database
\dt - display any available tables when connected to a database
\l - list available databases
\q - quit the current menu/quit psql
When connected to a database and running queries, remember to end the query with ;


{'ride_name_0': 'Colossus', 'year_opened_0': '2002', 'votes_0': '5', 'park_id_0': '1', 

'ride_name_1': 'Stealth', 'year_opened_1': '2006', 'votes_1': '4', 'park_id_1': '1', 

'ride_name_2': 'Loggers Leap', 'year_opened_2': '1989', 'votes_2': '9', 'park_id_2': '1', 'ride_name_3': 'Mr Monkeys Banana Ride', 'year_opened_3': '1994', 'votes_3': '5', 'park_id_3': '1', 'ride_name_4': 'Tidal Wave', 'year_opened_4': '2000', 'votes_4': '1', 'park_id_4': '1', 'ride_name_5': 'Rocky Express', 'year_opened_5': '1989', 'votes_5': '5', 'park_id_5': '1', 'ride_name_6': 'Nemesis', 'year_opened_6': '1994', 'votes_6': '5', 'park_id_6': '2', 'ride_name_7': 'The Smiler', 'year_opened_7': '2013', 'votes_7': '1', 'park_id_7': '2', 'ride_name_8': 'Rita', 'year_opened_8': '2005', 'votes_8': '5', 'park_id_8': '2', 'ride_name_9': 'Congo River Rapids', 'year_opened_9': '1994', 'votes_9': '3', 'park_id_9': '2', 'ride_name_10': 'Enterprise', 'year_opened_10': '1984', 'votes_10': '5', 'park_id_10': '2', 'ride_name_11': 'Gallopers Carousel', 'year_opened_11': '1991', 'votes_11': '7', 'park_id_11': '2', 'ride_name_12': 'Rattlesnake', 'year_opened_12': '1998', 'votes_12': '11', 'park_id_12': '3', 'ride_name_13': 'Tiger Rock', 'year_opened_13': '2018', 'votes_13': '3', 'park_id_13': '3', 'ride_name_14': 'KOBRA', 'year_opened_14': '2010', 'votes_14': '1', 'park_id_14': '3', 'ride_name_15': 'Tiny Truckers', 'year_opened_15': '1994', 'votes_15': '2', 'park_id_15': '3', 'ride_name_16': 'The Demon', 'year_opened_16': '2004', 'votes_16': '8', 'park_id_16': '4', 'ride_name_17': 'The Caravan', 'year_opened_17': '1974', 'votes_17': '1', 'park_id_17': '4', 'ride_name_18': 'The Bumper Cars', 'year_opened_18': '1926', 'votes_18': '25', 'park_id_18': '4', 'ride_name_19': 'The Little Pilot', 'year_opened_19': '1990', 'votes_19': '6', 'park_id_19': '4'}INSERT INTO parks 
(park_id, park_name, year_opened, annual_attendance) 
