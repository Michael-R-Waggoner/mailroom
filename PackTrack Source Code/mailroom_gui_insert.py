import sqlite3
import tkinter
from sqlite3 import Error
from datetime import date

# DB interactions
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

# Inserts package information to DB
def new_package(conn):
    try:
        sql = """INSERT INTO mail(recipient_name,tracking_number,receive_date,clerk_initials,courier)
                 VALUES(?,?,?,?,?)"""
        cur = conn.cursor()
        date_received = date.today()
        package = (f"{recipient_name.get()}",f"{tracking_num.get()}",f"{date_received}",f"{clerk_initials.get()}",f"{clicked.get()}")
        cur.execute(sql,package)
        conn.commit()
        confirmation = tkinter.Label(text=f"{recipient_name.get()},{tracking_num.get()},{date_received},{clerk_initials.get()},{clicked.get()} added to database.")
        confirmation.pack()
    except Exception as e:
        print(e)

# Clears fields after every entry
def clear_fields():
    recipient_name.delete(0, 200)
    tracking_num.delete(0, 200)
    clerk_initials.delete(0,200)

# Main function that orchestrates program
def main():
    database = "C:/sqlite/db/pythonsqlite.db"
    conn = create_connection(database)
    with conn:
        new_package(conn)
        clear_fields()

#Gui initialization==========================================
#Window Setup
window = tkinter.Tk()
window.title("MailPackTrack")

#Banner Label
banner = tkinter.Label(window,text="Welcome to the USMAPS PackTracker please enter package info below.",font=("Arial",16,"bold"))
banner.pack()

#Recipient name label for entry box
recipient_name_label = tkinter.Label(text="Recipient Name",padx=10,pady=10)
recipient_name_label.pack()

#Recipient name entry box to be passed to insert function
recipient_name = tkinter.Entry(window,name="recipient Name")
recipient_name.pack()

#tracking number label for entry box
tracking_num_label = tkinter.Label(text="Tracking Number",padx=10,pady=10)
tracking_num_label.pack()

#tracking number entry box to be passed to insert function
tracking_num = tkinter.Entry(window, name="tracking number")
tracking_num.pack()

#clerk intials label
clerk_initials_label = tkinter.Label(text="Clerk Initials")
clerk_initials_label.pack()

#clerk intials entry box
clerk_initials = tkinter.Entry(window,name="clerk intials")
clerk_initials.pack()

#Courier Options
options = [
    "USPS",
    "FEDEX",
    "UPS",
    "AMAZON",
    "EXPRESS MAIL",
    "REGISTERED MAIL",
    "INSURED MAIL",
    "CERTIFIED MAIL",
    "SIGNATURE CONFIRMATION",
    "DHL"
]

#Label for dropdown menu
courier_label = tkinter.Label(text="Select courier service from dropdown options.",padx=10,pady=10)
courier_label.pack()

#dropdown courier entry to be passed to insert function
clicked = tkinter.StringVar()
clicked.set("USPS")
courier = tkinter.OptionMenu(window, clicked,*options)
courier.pack()

# Submit Button setup
submit_button = tkinter.Button(window,text="Submit", command=main,padx=10,pady=10)
submit_button.pack()


window.mainloop()