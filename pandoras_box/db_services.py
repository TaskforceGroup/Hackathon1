# This is a function for getting things from and saving things to it

"""
This file is for interacting with the database
The dummy data will slowly get replaced as the database it built out
The following global vars will be deleted as we are able to interact with the database

Make sure to format the data from the database here to match 
"""
GROUPS = {
    'groups': [
            {'name': 'Group A', 'description': 'Dedicated to finding Nick guilty', 'data': [
                    'look at stars', 'Eat donuts', 'Play LOL'
                ]
            },
            {'name': 'Group B with a longer name', 'description': 'Free food events', 'data': [
                    'Going to Walmart', 'Went to gym', 'look at rocks'
                ]
            }
        ]
    }


def get_all_groups():
    return GROUPS


def get_groups_by_id(id=None):
    """
    Get all of the groups in a structure like JSON.
    It should get the group with the particular ID if specified
    """
    return GROUPS

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
    pass

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
