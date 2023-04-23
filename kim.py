import sqlite3
import pandas as pd

conn = sqlite3.connect("hackathon.db")

def update_dates(table_name):
    query = f"SELECT * FROM {table_name} WHERE event_date LIKE '44%'"
    df = pd.read_sql_query(query, conn)
    
    # Convert the 'event_date' column to a numeric type
    df['event_date'] = pd.to_numeric(df['event_date'], errors='coerce')

    df['event_date'] = pd.to_datetime(df['event_date'], unit='D', origin='1899-12-30')
    df['event_date'] = df['event_date'].dt.strftime('%m/%d/%Y')

    df.to_sql(table_name, conn, if_exists='replace', index=False)


table_names = [
    'dim_device_locations',
    'dim_charge_status',
    'dim_power_status',
    'dim_lock_status'
]

for table_name in table_names:
    update_dates(table_name)

conn.commit()

conn.close()
