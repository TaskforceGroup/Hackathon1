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



def get_groups():
    """
    Get all of the groups in a structure like JSON
    """
    return GROUPS

def new_group(name, description):
    """
    Add a group
    """
    GROUPS['groups'].append(
            {'name': name, 'description': description, 'data': [] # No data yet
            }
        )


