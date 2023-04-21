# This is a function for getting things from and saving things to it
import duckdb
"""
This file is for interacting with the database
The dummy data will slowly get replaced as the database it built out
The following global vars will be deleted as we are able to interact with the database

Make sure to format the data from the database here to match 
"""
# create connection to sqlite database
conn = duckdb.connect('hackathon.db')
groups = dict(conn.sql('SELECT DISTINCT group_id, name FROM groups').df())


def get_all_groups():
    return GROUPS


def get_groups_by_id(id=None):
    """
    Get all of the groups in a structure like JSON.
    It should get the group with the particular ID if specified
    """
    return groups

def new_group(name, description=None):
    """
    Add a group. Description can be blank.
    """
    pass # Return the 

def edit_group(id, new_name, new_description=None):
    pass


# --- --- --- Events, things like sms, calls, and log_events --- --- ---

def get_all_events(sms=False, calls=False, log_events=False):
    pass

def get_event_by_id(id, table, sms=False, calls=False, log_events=False):
    max_id = conn.sql('SELECT MAX(group_id) FROM groups')
    group_occurrences = conn.sql(f'SELECT COUNT(group_id) FROM groups WHERE name = {name}')
    conn.sql(f'INSERT INTO groups VALUES({max_id+1}, {name}, {description}, {group_occurrences+1})')

def get_event_by_type():
    pass


"""
The whiteboard notes

create group
get_groups
get_all_groups

time_start
time_end
data_type
data_size
text_seen

item -> description
get_items (start_date, end_date, exact_date)

edit_item(item_id, new_name=None, new_description=None
add_item_to_group(item_id, group_id)

"""
