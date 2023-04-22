# Import all necessary libraries
import duckdb
import pandas as pd
"""
This file is for interacting with the database
The dummy data will slowly get replaced as the database it built out
The following global vars will be deleted as we are able to interact with the database

Make sure to format the data from the database here to match 
"""
# Convert OLTP Database to OLAP
conn = duckdb.connect('hackathon.db')


def get_all_groups():
    
    query = conn.sql('SELECT DISTINCT group_id, name, description FROM groups').df()
    return query.to_json()

def get_groups_by_id(id=None):

    query = conn.sql(f'SELECT DISTINCT group_id, name, description FROM groups WHERE group_id IN({id})')
    return query.to_json()

def new_group(name, description=None):
    max_id = conn.sql('SELECT MAX(group_id) FROM groups')
    conn.sql(f'''INSERT INTO groups VALUES({max_id+1}, '{name}', '{description}')''')
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
