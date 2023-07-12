import psycopg2
import PySimpleGUI as sg
#connect to local server
mydb = psycopg2.connect(database="postgres", user = "postgres", password = "2005", host = "localhost", port = "5432")
mycursor = mydb.cursor()
def create_table():
    mycursor.execute('''CREATE TABLE IF NOT EXISTS contact(NAME TEXT NOT NULL,JOB TEXT NOT NULL,SEX TEXT NOT NULL,Phonenumber INT NOT NULL)''')

create_table()
#Function to insert contact into the dbms
def insert(name, job, sex, phone):
 insert = "INSERT INTO contact (name, job, sex, phonenumber) VALUES(%s,%s,%s,%s)"
 data = (name, job, sex, phone)
 mycursor.execute(insert,data)
 print("Contact is added")
 mydb.commit()

#Function to view all contact 
def showContact():
 mycursor.execute("SELECT * FROM contact ORDER BY name ASC")
 myresult = mycursor.fetchall()
 print("The contact list")
 for x in myresult:
  print(x)

#function that view only specific name
def showOnly(name):
 sql = "SELECT * FROM contact WHERE name = %s"
 mycursor.execute(sql, (name,))
 result = mycursor.fetchone()
 print(result)

#function that we use to delete the contact
def delcontact(name):
 sql = "DELETE FROM contact WHERE name = %s"
 mycursor.execute(sql, (name,))
 print("User is deleted")
 mydb.commit()

#Set the theme for the window
sg.theme('LightYellow')

#The UI layout that user will see
layout = [
    [sg.Text("Name:"), sg.Input(key="-NAME-")],
    [sg.Text("Job:"), sg.Input(key="-JOB-")],
    [sg.Text("Sex:"), sg.Input(key="-SEX-")],
    [sg.Text("Phone Number:"), sg.Input(key="-PHONE-")],
    [sg.Button("Insert Contact"), sg.Button("Delete Contact"), sg.Button("Show Contact"), sg.Button("Search Contact by Name")],
    [sg.Output(size=(50,10))]
]

window = sg.Window("Contact Manager", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "Insert Contact":
        name = values["-NAME-"]
        job = values["-JOB-"]
        sex = values["-SEX-"]
        phone = values["-PHONE-"]
        insert(name, job, sex, phone)
        showContact()
        #Clear the input fields after inserting a contact
        window["-NAME-"].update("")
        window["-JOB-"].update("")
        window["-SEX-"].update("")
        window["-PHONE-"].update("")
    elif event == "Delete Contact":
        name = values["-NAME-"]
        delcontact(name)
        #Clear the input field after deleting a contact
        window["-NAME-"].update("")
    elif event == "Show Contact":
        showContact()
    elif event == "Search Contact by Name":
        name = values["-NAME-"]
        showOnly(name)
        #Clear the input field after searching a contact
        window["-NAME-"].update("")

window.close()
