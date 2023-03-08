# mySQL-DB-injector-connector

This code is a Python program that creates a GUI window using the tkinter library, which allows the user to enter MySQL database credentials and insert dummy data into a MySQL database. Here are the steps the program takes:

Import the necessary libraries: mysql.connector, Error, tkinter, and messagebox.
Create a GUI window using tkinter with the title "Insert Dummy Data into MySQL" and a size of 400x250.
Create four label and text entry fields using tkinter for the user to input their MySQL username, password, database name, and location.
Define a function called insert_dummy_data() that extracts the user input from the text entry fields, connects to the MySQL database using the input credentials, inserts dummy data into a table named "staff", and displays a success or error message box using tkinter's messagebox module.
Create a button labeled "Insert Dummy Data" that executes the insert_dummy_data() function when clicked.
Run the tkinter event loop to display the window and wait for user interaction.
