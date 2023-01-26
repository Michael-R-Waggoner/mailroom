import sqlite3
import tkinter
from sqlite3 import Error
from PIL import Image, ImageDraw
from datetime import date

window = tkinter.Tk()
window.title("MailPackTrack")

cvs = tkinter.Canvas(window, width=500,height=50, highlightthickness=10,bg="white")
cvs.grid(column=2,row=3)

#Connects to DB============================================================================
mousePressed = False
last = None

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

#Signature acceptance======================================================================
def press(evt):
    global mousePressed
    mousePressed = True
def release(evt):
    global mousePressed
    mousePressed = False
cvs.bind_all('<ButtonPress-1>', press)
cvs.bind_all('<ButtonRelease-1>', release)

def finish():
    img.save('img.png')
    with open("img.png","rb") as image:
        global converted_string
        converted_string = image.read()



def move(evt):
    global mousePressed, last
    x,y = evt.x,evt.y
    if mousePressed:
        if last is None:
            last = (x,y)
            return
        draw.line(((x,y),last), (0,0,0))
        cvs.create_line(x,y,last[0],last[1])
        last = (x,y)
    else:
        last = (x,y)

cvs.bind_all('<Motion>', move)

# Inserts package information to DB==========================================================
def update_package(conn):
    try:
        sql = """UPDATE mail SET date_delivered = ?,
                                 signature = ?
                 WHERE tracking_number = ?;"""
        cur = conn.cursor()
        date_delivered = date.today()
        package = (f"{date_delivered}",converted_string,f"{tracking_num.get()}")
        cur.execute(sql,package)
        conn.commit()
        confirmation = tkinter.Label(text=f"{date_delivered},{tracking_num.get()}, and signature added to database.")
        confirmation.grid(row=5,column=2)
    except Exception as e:
        print(e)
    
# Clears insert fields
def clear_fields():
    tracking_num.delete(0, 200)

#Orchestrates functionality
def main():
    database = "C:/sqlite/db/pythonsqlite.db"
    conn = create_connection(database)
    with conn:
        finish()
        update_package(conn)
        clear_fields()


# UPDATE mail date_delivered = 123 WHERE tracking_number = 123;
#GUI setup ==========================================================================

#creates image object to be encoded
img = Image.new('RGB',(500,500),(255,255,255))
draw = ImageDraw.Draw(img)

#label for signature block
sig_label = tkinter.Label(window, text="Signature")
sig_label.grid(column=1,row=3)

#Creates banner image for GUI
banner = tkinter.Label(window,wrap="500",text="Welcome to the USMAPS PackTracker please enter info below. Enter Tracking number, signature, and delivery date to update database.",font=("Arial",14,"bold"))
banner.grid(column=2,row=1)

#Creates Label for tracking_num field
tracking_num_label = tkinter.Label(window, text="Tracking Number")
tracking_num_label.grid(column=1,row=2)

#Accepts tracking_num to be passed to db
tracking_num = tkinter.Entry(window)
tracking_num.grid(column=2,row=2)

#Creates Submit button that starts main funciton
submit = tkinter.Button(window, text="Submit", command=main)
submit.grid(column=3,row=3)

window.mainloop()