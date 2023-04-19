import sqlite3

# establish connection to OLTP database
conn = sqlite3.connect('hackathon.db')
c = conn.cursor()

# create DEVICES table
c.execute('''
          CREATE TABLE IF NOT EXISTS devices (device_id INTEGER PRIMARY KEY, product_name VARCHAR(50) NOT NULL, serial_number VARCHAR(50) NOT NULL, model_number VARCHAR(50) NOT NULL, software_version VARCHAR(50) NOT NULL)
          ''')

# create CONTACTS table
c.execute('''
          CREATE TABLE IF NOT EXISTS contacts (device_id INTEGER NOT NULL, contact_num INTEGER NOT NULL, first_name VARCHAR(50) NOT NULL, last_name VARCHAR(50) NOT NULL, date_added TEXT NOT NULL, time_added TEXT NOT NULL, home_phone VARCHAR(15), cell_phone VARCHAR(15), work_phone VARCHAR(15), email VARCHAR(50), FOREIGN KEY (device_id) REFERENCES devices (device_id), PRIMARY KEY(device_id, contact_num))
          ''')

# create SENDERS table
c.execute('''
          CREATE TABLE IF NOT EXISTS senders (sender_id INTEGER PRIMARY KEY, name VARCHAR(100) NOT NULL, username VARCHAR(100), FOREIGN KEY(sender_id) REFERENCES devices(device_id))
          ''')

# create RECEIVERS table
c.execute('''
          CREATE TABLE IF NOT EXISTS receivers (receiver_id INTEGER PRIMARY KEY, name VARCHAR(100) NOT NULL, username VARCHAR(100), FOREIGN KEY (receiver_id) REFERENCES devices (device_id))
          ''')

# create SMS_MESSAGES table
c.execute('''
          CREATE TABLE IF NOT EXISTS sms_messages (message_id INTEGER PRIMARY KEY, send_date TEXT, send_time TEXT, content TEXT, sender_id INTEGER NOT NULL, receiver_id INTEGER NOT NULL, FOREIGN KEY (sender_id) REFERENCES senders (sender_id), FOREIGN KEY (receiver_id) REFERENCES receivers (receiver_id))
          ''')

# create CALLS table
c.execute('''
          CREATE TABLE IF NOT EXISTS calls (call_id INTEGER PRIMARY KEY, call_date TEXT, call_time TEXT, length_seconds INTEGER, status VARCHAR(25), sender_id INTEGER NOT NULL, receiver_id INTEGER NOT NULL, FOREIGN KEY (sender_id) REFERENCES senders (sender_id), FOREIGN KEY (receiver_id) REFERENCES receivers (receiver_id), CHECK (status IN('Accepted', 'Missed', 'Rejected')))
          ''')

# create INSTANT_MESSAGES table
c.execute('''
          CREATE TABLE IF NOT EXISTS instant_messages (message_id INTEGER PRIMARY KEY, send_date TEXT, send_time TEXT, platform VARCHAR(25), viewed BOOLEAN, content TEXT, sender_id INTEGER NOT NULL, receiver_id INTEGER NOT NULL, FOREIGN KEY (sender_id) REFERENCES senders (sender_id), FOREIGN KEY (receiver_id) REFERENCES receivers (receiver_id), CHECK ( platform IN('Messenger', 'SnapChat', 'WhatsApp', 'Discord', 'Slack')))
          ''')

# create LOCATION table
c.execute('''
          CREATE TABLE IF NOT EXISTS location (device_id INTEGER NOT NULL, gps_date TEXT NOT NULL, gps_time TEXT NOT NULL, latitude INTEGER NOT NULL, longitude INTEGER NOT NULL, latitude_direction VARCHAR(15) NOT NULL, longitude_direction VARCHAR(15), FOREIGN KEY (device_id) REFERENCES devices (device_id), PRIMARY KEY(device_id, gps_date, gps_time),  CHECK (latitude_direction IN('North', 'South')), CHECK (longitude_direction IN('West', 'East')))
          ''')

# create POWER_STATUS table
c.execute('''
          CREATE TABLE IF NOT EXISTS power_status (device_id INTEGER NOT NULL, power_date TEXT NOT NULL, power_time TEXT NOT NULL, powered_on BOOLEAN NOT NULL, FOREIGN KEY (device_id) REFERENCES devices (device_id), PRIMARY KEY(device_id, power_date, power_time))
          ''')

# create LOCK_STATUS table
c.execute('''
          CREATE TABLE IF NOT EXISTS lock_status (device_id INTEGER NOT NULL, lock_date TEXT NOT NULL, lock_time TEXT NOT NULL, locked BOOLEAN, FOREIGN KEY (device_id) REFERENCES devices (device_id), PRIMARY KEY(device_id, lock_date, lock_time))
          ''')

# create LOGINS table
c.execute('''
          CREATE TABLE IF NOT EXISTS logins (device_id INTEGER NOT NULL, login_date TEXT NOT NULL, login_time TEXT NOT NULL, attempt_number INTEGER, successful BOOLEAN, login_method VARCHAR(25) NOT NULL, FOREIGN KEY (device_id) REFERENCES devices (device_id), CHECK ( login_method IN('PIN', 'Password', 'Fingerprint', 'Facial Recognition')), PRIMARY KEY(device_id, login_date, login_time))
          ''')

# create CHARGE_STATUS table
c.execute('''
          CREATE TABLE IF NOT EXISTS charge_status (device_id INTEGER NOT NULL, charge_date TEXT NOT NULL, charge_time TEXT NOT NULL, FOREIGN KEY (device_id) REFERENCES devices (device_id), PRIMARY KEY(device_id, charge_date, charge_time))
          ''')

# create CABLE_CONNECTIONS table
c.execute('''
          CREATE TABLE IF NOT EXISTS cable_connections (device_id INTEGER NOT NULL, connection_date TEXT NOT NULL, connection_time TEXT NOT NULL, PRIMARY KEY(device_id, connection_date, connection_time), FOREIGN KEY (device_id) REFERENCES devices (device_id))
          ''')

# create BLUETOOTH_CONNECTIONS table
c.execute('''
          CREATE TABLE IF NOT EXISTS bluetooth_connections (device_id INTEGER NOT NULL, connection_date TEXT NOT NULL, connection_time TEXT NOT NULL, device_type VARCHAR(25) NOT NULL, FOREIGN KEY (device_id) REFERENCES devices (device_id), CHECK (device_type IN('Speaker', 'Monitor', 'Watch', 'IoT Device')), PRIMARY KEY(device_id, connection_date, connection_time))
          ''')

# create ON_BODY_STATUS table
c.execute('''
          CREATE TABLE IF NOT EXISTS on_body_status (device_id INTEGER NOT NULL, on_body_date TEXT NOT NULL, on_body_time TEXT NOT NULL, on_body BOOLEAN NOT NULL, FOREIGN KEY (device_id) REFERENCES devices (device_id), PRIMARY KEY(device_id, on_body_date, on_body_time))
          ''')