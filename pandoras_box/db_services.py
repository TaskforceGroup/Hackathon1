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
GROUPS = conn.sql('SELECT DISTINCT group_id, name FROM groups')



def get_groups():
    """
    Get all of the groups in a structure like JSON
    """
    return GROUPS

def new_group(name, description):
    """
    Add a group
    """
    max_id = conn.sql('SELECT MAX(group_id) FROM groups')
    group_occurrences = conn.sql(f'SELECT COUNT(group_id) FROM groups WHERE name = {name}')
    conn.sql(f'INSERT INTO groups VALUES({max_id+1}, {name}, {description}, {group_occurrences+1})')


