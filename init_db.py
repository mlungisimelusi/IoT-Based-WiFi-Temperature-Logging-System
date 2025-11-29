import sqlite3

# Connect to (or create) the database file
conn = sqlite3.connect('iot_data.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create the 'logs' table if it doesn't exist
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS logs (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         temperature REAL NOT NULL,
#         humidity REAL NOT NULL,
#         timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
#     )
# ''')
cursor.execute('''
   CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    temperature REAL NOT NULL,
    humidity REAL NOT NULL,
    timestamp TEXT NOT NULL
);
''')

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database and table created successfully.")
