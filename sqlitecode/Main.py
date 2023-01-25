import tkinter
from subprocess import run

def start_db():
    run(["./db_init.exe"])

def receive_package():
    run(["./mailroom_gui_insert.exe"])

def update_mail():
    run(["./Edit_Mail.exe"])

def query():
    run(["./query.exe"])

def request_signature():
    run(["./signature_request.exe"])
#GUI Setup====================================================================================================
window = tkinter.Tk()
window.title("PackTrack Home Screen")

#creates banner label
banner = tkinter.Label(text="Welcome to USMAPS PackTrack please choose an option.",font=("arial",12,"bold"))
banner.pack()

#creates background image
canvas = tkinter.Canvas(width=300,height=246,highlightthickness=0)
photo = tkinter.PhotoImage(file="./Usmaps_crest.gif")
canvas.create_image(150,123,image=photo)
canvas.pack()

#creates receive button
receive_button = tkinter.Button(text="Enter New Packages", command=receive_package)
receive_button.pack()

#Creates update button
update_button = tkinter.Button(text="Add Delivery Date and Signature to a package", command=update_mail)
update_button.pack()

#Query Button
query_button = tkinter.Button(text="Query the Database",command=query)
query_button.pack()

#Create signature request button
signature_request_button = tkinter.Button(text="Retrieve Signature",command=request_signature)
signature_request_button.pack()

#Creates start db button
start_dbase = tkinter.Button(text="Initialize a new Database",command=start_db)
start_dbase.pack()

window.mainloop()