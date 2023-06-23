#Import the mysql dictionary
import mysql.connector
import PySimpleGUI as sg

sg.theme('DarkGreen3')

#connect to local server
mydb = mysql.connector.connect(
  host="localhost",
  user="heang",
  password="2005",
  database = "contact"
)
mycursor = mydb.cursor()

#Function to insert contact into the dbms
def insert(name, job, sex, phonenumber):
 insert = "INSERT INTO contact (name, job, sex, phonenumber) VALUES(%s,%s,%s,%s)"
 data = (name, job, sex, phonenumber)
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

#The UI layout that user will see
layout = [
    [sg.Text("Name:"), sg.Input(key="-NAME-")],
    [sg.Text("Job:"), sg.Input(key="-JOB-")],
    [sg.Text("Sex:"), sg.Input(key="-SEX-")],
    [sg.Text("Phone Number:"), sg.Input(key="-PHONE-")],
    [sg.Button("Insert Contact"), sg.Button("Delete by Name Contact"), sg.Button("Show Contact"), sg.Button("Search Contact by Name")],
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
