import pytest
from db.seed import seed
from db.connection import create_conn, close_db
from db.data.index import index as data
from db.utils.format_rides import utils_park_names_to_id, prepare_rides_data


# https://l2c.northcoders.com/courses/de-notes/de2-fundamentals-testing#sectionId=,step=
# https://docs.python.org/3/library/unittest.mock.html


@pytest.fixture(scope="session")
def db():
    '''Runs seed before starting tests. 
       Yields a database connection object to be used in tests. 
       Closes connection to db after tests have ran'''
    test_db = create_conn()
    seed(test_db, **data)
    yield test_db
    close_db(test_db)

def test_parks_query_is_a_list_of_lists(db):
    # Assign
    base_query = "SELECT * FROM parks"
    
    # Act
    expected = db.run(base_query)

    # Act 
    assert isinstance(expected, list)
    assert isinstance(expected[0], list)
    assert isinstance(expected[1], list)
    assert [1, 'Thorpe Park', 1979, 1700000] in expected
    assert [2, 'Alton Towers', 1980, 2520000] in expected


def test_utils_func_returns_a_dict():
    test_output = utils_park_names_to_id()

    assert isinstance(test_output, dict)

def test_columns_of_db_query_are_for_parks_data(db):

    db.run("SELECT * FROM parks")

    assert 'park_id' == db.columns[0]['name']
    assert 'park_name' == db.columns[1]['name']
    assert 'year_opened' == db.columns[2]['name']
    assert 'annual_attendance' == db.columns[3]['name']

def test_rows_output_data_from_parks_table(db):
    db_query = db.run("SELECT * FROM parks")

    row_1 = db_query[0]
    row_2 = db_query[1]
    row_3 = db_query[2]
    row_4 = db_query[3]

    assert row_1 == [1, 'Thorpe Park', 1979, 1700000]
    assert row_2 == [2, 'Alton Towers', 1980, 2520000]
    assert row_3 == [3, 'Chessington World of Adventures', 1987, 1400000]
    assert row_4 == [4, 'Tivoli Gardens', 1843, 3972000]

def test_park_ids_and_names_are_collected_from_db(db):
    db_query_ids = db.run("SELECT park_id FROM parks;")
    db_query_names = db.run("SELECT park_name FROM parks;")

    assert db_query_ids[0][0] == 1
    assert db_query_ids[1][0] == 2
    assert db_query_ids[2][0] == 3
    assert db_query_ids[3][0] == 4
    assert db_query_names[0][0] == 'Thorpe Park'
    assert db_query_names[1][0] == 'Alton Towers'
    assert db_query_names[2][0] == 'Chessington World of Adventures'
    assert db_query_names[3][0] == 'Tivoli Gardens'

def test_utils_func_maps_park_names_to_ids(db):
    db_query_ids = db.run("SELECT park_id FROM parks;")
    db_query_names = db.run("SELECT park_name FROM parks;")

    utils_func = utils_park_names_to_id()

    assert utils_func[db_query_names[0][0]] == db_query_ids[0][0]
    assert utils_func[db_query_names[1][0]] == db_query_ids[1][0]
    assert utils_func[db_query_names[2][0]] == db_query_ids[2][0]
    assert utils_func[db_query_names[3][0]] == db_query_ids[3][0]