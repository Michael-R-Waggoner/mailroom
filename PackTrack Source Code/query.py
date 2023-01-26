import sqlite3
from sqlite3 import Error
import tkinter
import tkinter.messagebox

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

#Queries database based on dropdown selection
def query_db(conn,query):
    if clicked.get() == "tracking_number":
        sql = "SELECT id, recipient_name,tracking_number,receive_date,clerk_initials,courier,date_delivered FROM mail WHERE tracking_number = ?"
    elif clicked.get() == "recipient_name":
        sql = "SELECT id, recipient_name,tracking_number,receive_date,clerk_initials,courier,date_delivered FROM mail WHERE recipient_name = ?"
    elif clicked.get() == "receive_date":
        sql = "SELECT id, recipient_name,tracking_number,receive_date,clerk_initials,courier,date_delivered FROM mail WHERE receive_date = ?"
    elif clicked.get() == "courier":
        sql = "SELECT id, recipient_name,tracking_number,receive_date,clerk_initials,courier,date_delivered FROM mail WHERE courier = ?"
    elif clicked.get() == "date_delivered":
        sql = "SELECT id, recipient_name,tracking_number,receive_date,clerk_initials,courier,date_delivered FROM mail WHERE date_delivered = ?"
    elif clicked.get() == "clerk_initials":
        sql = "SELECT id, recipient_name,tracking_number,receive_date,clerk_initials,courier,date_delivered FROM mail WHERE clerk_initials = ?"
    cur = conn.cursor()
    cur.execute(sql,query)
    rows = cur.fetchall()
    #This loop stores output to a list to enable more effective clearing later on
    global output
    output = []
    for i in range(0,len(rows)):
        output.append(tkinter.Label(text=f"{rows[i]}"))
        output[i].pack()

#queries entire database and returns all rows except for the signature column
def query_db_all():
    database = "C:/sqlite/db/pythonsqlite.db"
    conn = create_connection(database)
    sql = "SELECT id, recipient_name,tracking_number,receive_date,clerk_initials,courier,date_delivered FROM mail"
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    #This loop stores output to a list to enable more effective clearing later on
    window2 = tkinter.Tk()
    global output
    output = []
    for i in range(0,len(rows)):
        output.append(tkinter.Label(window2, text=f"{rows[i]}"))
        output[i].pack()
    window2.mainloop()

def clear_output():
    for label in output:
        label.pack_forget()

#orchestrates query functions
def main():
    database = "C:/sqlite/db/pythonsqlite.db"
    conn = create_connection(database)
    with conn:
        query = (f"{search_term.get()}",)
        query_db(conn,query)
        

#GUI Setup========================================================================
window = tkinter.Tk()
window.title("Database Query")

banner = tkinter.Label(text="Please select a query option from the drop down menu and enter search term. Please use exact spelling and the search is case-sensitive. Also please clear previous queries before entering new ones.",wraplength=500,font=("arial",12,"bold"))
banner.pack()

#Query Options
options = [
    "tracking_number",
    "recipient_name",
    "receive_date",
    "clerk_initials",
    "courier",
    "date_delivered"
]

#Label for dropdown menu
query_label = tkinter.Label(text="Select query parameter from dropdown options.",padx=10,pady=10)
query_label.pack()

#dropdown query entry to be passed to insert function
clicked = tkinter.StringVar()
clicked.set("tracking_number")
query_param = tkinter.OptionMenu(window, clicked,*options)
query_param.pack()

#Label for input box
search_term_label = tkinter.Label(text="Search Term:")
search_term_label.pack()

#Input box for search term
search_term  = tkinter.Entry()
search_term.pack()

#Creates button to submit query
submit_button = tkinter.Button(text="Submit",command=main)
submit_button.pack()

#Creates query all button
query_all_button = tkinter.Button(text="Show all entries in Database", command=query_db_all)
query_all_button.pack()

#Clear queries button
clear_query_button = tkinter.Button(text="Clear previous queries",command=clear_output)
clear_query_button.pack()

window.mainloop()