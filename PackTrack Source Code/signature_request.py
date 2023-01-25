import sqlite3
import tkinter
import PIL.Image as Image
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

# This opens a file to have bytes written into and then reopened and saved as a usable .png
def decode_image(img):
    with open(f".\{tracking_number.get()}signature.png","wb") as fh:
        fh.write(img)
    im = Image.open(f".\{tracking_number.get()}signature.png")
    im.save(f".\{tracking_number.get()}signature.png")

def query_image(conn,query):
    sql = "SELECT * FROM mail WHERE tracking_number = ?"
    cur = conn.cursor()
    cur.execute(sql,query)
    data_raw = cur.fetchone()
    data = data_raw[7]
    global everything_else
    everything_else = data_raw[:-1]
    return data


def report():
    window2 = tkinter.Tk()
    window2.title("Result")
    window.config(width=500,height=200)
    banner = tkinter.Label(window2, wraplength=500,text=f"Here is the primary id, recipient name, tracking number, receive date, clerk initials, courier, date delivered and signature associated with {tracking_number.get()}: \n {everything_else}",font=("arial",14,"bold"))
    banner.pack()
    canvas = tkinter.Canvas(window2, width=500,height=100,highlightthickness=0)
    photo = tkinter.PhotoImage(master=canvas,file=f".\{tracking_number.get()}signature.png")
    canvas.create_image(250,250,image=photo)
    canvas.pack()
    confirmation = tkinter.Label(window2, text=f"Image has been saved to .\{tracking_number.get()}.png.")
    confirmation.pack()
    window2.mainloop()


#orchestrates query and decode functions
def main():
    database = "C:/sqlite/db/pythonsqlite.db"
    conn = create_connection(database)
    with conn:
        query = (f"{tracking_number.get()}",)
        img = query_image(conn,query)
        decode_image(img)
        report()
        
        
#GUI Setup=====================================================================================================================
window = tkinter.Tk()
window.title("Signature Retrieval")

banner = tkinter.Label(window, text="Please input tracking number related to signature.", font=("arial",12,"bold"))
banner.pack()

tracking_number = tkinter.Entry(window)
tracking_number.pack()

submit_button = tkinter.Button(window, text="Submit",command=main)
submit_button.pack()

window.mainloop()