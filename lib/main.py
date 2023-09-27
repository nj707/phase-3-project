import os;
import tkinter as tk
import sqlite3
from tabulate import tabulate


# Create a database connection and cursor
CONN = sqlite3.connect('user_accounts.db')
CURSOR = CONN.cursor()

# Create a table for user accounts if it doesn't exist
CURSOR.execute('''CREATE TABLE IF NOT EXISTS accounts (
                id INTEGER PRIMARY KEY,
                username TEXT,
                password TEXT
            )''')
CONN.commit()

username_entry = ''
password_entry = ''
# Function to create a user account and open the clothing item addition interface
def create_account():
    username = username_entry.get()
    password = password_entry.get()

    if username and password:
        CURSOR.execute("INSERT INTO accounts (username, password) VALUES (?, ?)",
                    (username, password))
        CONN.commit()
        status_label.config(text="Account created successfully")

        # Close the account creation window
        root.destroy()

        # Open the clothing item addition window
        open_clothing_window()
    else:
        status_label.config(text="Please fill in both username and password fields")

# Function to open the clothing item addition interface
def open_clothing_window():
    # Create a new window for adding clothing items
    clothing_root = tk.Tk()
    clothing_root.title("Clothing Inventory")

    # Rest of the code for the clothing item addition interface (similar to the previous example)

    # Start the clothing item addition GUI application
    clothing_root.mainloop()

# Create the main window for account creation
root = tk.Tk()
root.title("Account Creation")

root.mainloop()

CONN = sqlite3.connect('clothing.db')
CURSOR = CONN.cursor()

# Create a table for clothing items if it doesn't exist
CURSOR.execute('''CREATE TABLE IF NOT EXISTS clothing (
                id INTEGER PRIMARY KEY,
                item_name TEXT,
                category TEXT,
                color TEXT,
                size TEXT
            )''')
CONN.commit()

# Function to add a clothing item to the database
def add_clothing():
    item_name = item_name_entry.get()
    category = category_entry.get()
    color = color_entry.get()
    size = size_entry.get()

    if item_name and category and color and size:
        CURSOR.execute("INSERT INTO clothing (item_name, category, color, size) VALUES (?, ?, ?, ?)",
                        (item_name, category, color, size))
        CONN.commit()
        status_label.config(text="Clothing item added successfully")
    else:
        status_label.config(text="Please fill in all fields")

# Create the main window
root = tk.Tk()
root.title("Clothing Inventory")

# Labels and Entry widgets for input
item_name_label = tk.Label(root, text="Item Name:")
item_name_label.pack()
item_name_entry = tk.Entry(root)
item_name_entry.pack()

category_label = tk.Label(root, text="Category:")
category_label.pack()
category_entry = tk.Entry(root)
category_entry.pack()

color_label = tk.Label(root, text="Color:")
color_label.pack()
color_entry = tk.Entry(root)
color_entry.pack()

size_label = tk.Label(root, text="Size:")
size_label.pack()
size_entry = tk.Entry(root)
size_entry.pack()

# Button to add clothing item
add_button = tk.Button(root, text="Add Clothing Item", command=add_clothing)
add_button.pack()

# Status label to display messages
status_label = tk.Label(root, text="")
status_label.pack()

# Start the GUI application
root.mainloop()



def menu ():
    os.system('cls||clear')
    print("+++++++++++++++++++++++++++++++")
    print("++                           ++")
    print("++            Menu           ++")
    print("++                           ++")
    print("+++++++++++++++++++++++++++++++")
    print("++                           ++")
    print("++ Welcome to python_stylist ++")
    print("++      First time here?     ++")
    print("++       Enter Y or N        ++")
    print("++                           ++")
    print("+++++++++++++++++++++++++++++++")
    account_input = input("Enter:")
    account_input = account_input.lower()
    if(account_input == "y"):
        account_creation()
    elif(account_input == "n"):
        os.system('cls||clear')
        account_view()
    else:
        os.system('cls||clear')
        print("Invalid input!")

    pass

def account_creation():
    os.system('cls||clear')
    print("++++++++++++++++++++++++++++++++++++++++++")
    print("++                                      ++")
    print("++            Account menu              ++")
    print("++                                      ++")
    print("++++++++++++++++++++++++++++++++++++++++++")
    print("++                                      ++")
    print("++  Would you like to make an account?  ++")
    print("++            Enter Y or N              ++")
    print("++                                      ++")
    print("++++++++++++++++++++++++++++++++++++++++++")
    account_create_input = input("Enter:")
    account_create_input = account_create_input.lower()
    if(account_create_input == "y"):
        print ("Radical!")
    else:
        print ("Have a good day!")
    pass
def account_view():
    os.system('cls||clear')
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("++                                        ++")
    print("++             Account menu               ++")
    print("++                                        ++")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("++                                        ++")
    print("++  Would you like to view your account?  ++")
    print("++             Enter Y or N               ++")
    print("++                                        ++")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    account_view_input = input("Enter:")
    account_view_input = account_view_input.lower()
    if(account_view_input == "y"):
        account_name_input = input("Please enter your name:")
        print (account_name_input)
    else:
        print("Have a good day!")


menu()

