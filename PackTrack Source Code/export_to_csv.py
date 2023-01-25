import pandas as pd
import sqlite3
from datetime import datetime
import getpass

db_file = "C:\sqlite\db\pythonsqlite.db"

table_name = "mail"

def get_run_time():
    # Get the current date and time
    run_time = datetime.now()
    return run_time.strftime("%Y-%m-%d")

# Connect to the database
con = sqlite3.connect(db_file)

# Read the table
df = pd.read_sql_query("SELECT * from {}".format(table_name), con)

# Write the dataframe to CSV
csv_file = df.to_csv(f"C:\\Users\\{getpass.getuser()}\\West Point\\Mail Room - Documents\\{get_run_time()}pythonsqlite.csv", index=False)

# Close the connection
con.close()
