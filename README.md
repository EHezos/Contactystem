# Contact Manager

This is a simple contact manager application built with Python, PostgreSQL, and PySimpleGUI.

## Features

- Create a table to store contacts
- Insert new contacts into the table  
- View all contacts
- Search for a specific contact by name
- Delete contacts
- Simple GUI for user interaction using PySimpleGUI

## Usage

The application connects to a local PostgreSQL database named `postgres` with user `postgres` and password `2005`. It will create a table called `contact` to store the contact details. 

The main GUI window has fields to enter a name, job, sex, and phone number to insert a new contact. It has buttons to insert, delete, view all, and search contacts.

The output of the queries and searches will be printed to the output box at the bottom.

## Requirements

- Python 3
- PostgreSQL  
- psycopg2 module
- PySimpleGUI

## Installation

Clone the repository:

```
git clone <repo URL>
```

Install requirements:

```
pip install -r requirements.txt
```

Run the application: 

```
python contact_manager.py
```

## Database Schema

The contact table has the following columns:

- NAME - Name of the contact (text, required)
- JOB - Job title of the contact (text, required)
- SEX - Gender of the contact (text, required)  
- PHONENUMBER - Phone number of the contact (integer, required)
  
## License

[MIT](LICENSE)
