# This is a function for getting things from and saving things to it

"""
This file is for interacting with the database
The dummy data will slowly get replaced as the database it built out
"""



def get_groups():
    data = {
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
    return data

def new_group(name, description):
    pass

