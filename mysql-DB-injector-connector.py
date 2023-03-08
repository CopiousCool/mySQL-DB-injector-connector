import mysql.connector
from mysql.connector import Error
import tkinter as tk
from tkinter import messagebox

# Create a GUI window using tkinter
window = tk.Tk()
window.title("Insert Dummy Data into MySQL")
window.geometry("400x250")

# Create label and text entry for MySQL username
lbl_username = tk.Label(window, text="MySQL Username:")
lbl_username.grid(column=0, row=0)
entry_username = tk.Entry(window, width=30)
entry_username.grid(column=1, row=0)

# Create label and text entry for MySQL password
lbl_password = tk.Label(window, text="MySQL Password:")
lbl_password.grid(column=0, row=1)
entry_password = tk.Entry(window, width=30, show="*")
entry_password.grid(column=1, row=1)

# Create label and text entry for database name
lbl_database = tk.Label(window, text="Database Name:")
lbl_database.grid(column=0, row=2)
entry_database = tk.Entry(window, width=30)
entry_database.grid(column=1, row=2)

# Create label and text entry for database location
lbl_location = tk.Label(window, text="Database Location:")
lbl_location.grid(column=0, row=3)
entry_location = tk.Entry(window, width=30)
entry_location.grid(column=1, row=3)

# Function to insert dummy data into staff table
def insert_dummy_data():
    # Get user inputs from text entries
    username = entry_username.get()
    password = entry_password.get()
    database = entry_database.get()
    location = entry_location.get()

    try:
        # Connect to MySQL database
        conn = mysql.connector.connect(host=location,
                                       database=database,
                                       user=username,
                                       password=password)
        if conn.is_connected():
            print('Connected to MySQL database')

            # Insert dummy data into staff table
            cursor = conn.cursor()
            sql = "INSERT INTO staff (staff_id, first_name, other_names, family_name, department, rate, start_date, manager) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            values = [
                (1, 'John', 'M', 'Doe', 'Sales', '50', '2021-01-01', 'Jane'),
                (2, 'Jane', '', 'Doe', 'Marketing', '60', '2021-02-01', 'John'),
                (3, 'Mary', '', 'Smith', 'Human Resources', '70', '2021-03-01', 'John'),
                (4, 'Tom', 'K', 'Lee', 'IT', '80', '2021-04-01', 'Jane')
            ]
            cursor.executemany(sql, values)
            conn.commit()
            print('Inserted data into staff table')
            messagebox.showinfo("Success", "Dummy data inserted successfully")

    except Error as e:
        print(e)
        messagebox.showerror("Error", "Error inserting dummy data: {}".format(e))

    finally:
        # Close database connection
        conn.close()
        print('Database connection closed')

# Create button to insert dummy data
btn_insert = tk.Button(window, text="Insert Dummy Data", command=insert_dummy_data)
btn_insert.grid(column=1, row=4)

# Run the tkinter event loop
window.mainloop()
