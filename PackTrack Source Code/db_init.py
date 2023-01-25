import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    database = "C:/sqlite/db/pythonsqlite.db"

    sql_create_mail_table =  """CREATE TABLE IF NOT EXISTS mail (
                                        id integer PRIMARY KEY,
	                                    recipient_name text,
	                                    tracking_number text,
	                                    receive_date text,
                                        clerk_initials text,
                                        courier text,
                                        date_delivered text,
                                        signature BLOB
                                    ); """
    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create mail table
        create_table(conn, sql_create_mail_table)
        conn.close()
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()