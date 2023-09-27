import tkinter as tk
import sqlite3

# Create a database connection and cursor
CONN = sqlite3.connect('user_accounts.db')
CURSOR = CONN.cursor()
add_clothing =""
# Create a table for user accounts if it doesn't exist
CURSOR.execute('''CREATE TABLE IF NOT EXISTS accounts (
                id INTEGER PRIMARY KEY,
                username TEXT,
                password TEXT
            )''')
CONN.commit()

# Create a table for clothing items if it doesn't exist
CONN.execute('''CREATE TABLE IF NOT EXISTS clothing (
                id INTEGER PRIMARY KEY,
                item_name TEXT,
                category TEXT,
                color TEXT,
                size TEXT
                
            )''')
CONN.commit()

# Function to create a user account
def create_account():
    username = username_entry.get()
    password = password_entry.get()

    if username and password:
        CURSOR.execute("INSERT INTO accounts (username, password) VALUES (?, ?)",
                    (username, password))
        CONN.commit()
        status_label.config(text="Account created successfully")
        # Switch to the clothing item addition menu
        switch_to_clothing_menu()
    else:
        status_label.config(text="Please fill in both username and password fields")

# Function to log in
def log_in():
    username = login_username_entry.get()
    password = login_password_entry.get()

    if username and password:
        CURSOR.execute("SELECT * FROM accounts WHERE username=? AND password=?", (username, password))
        account = CURSOR.fetchone()
        if account:
            status_label_login.config(text="Login successful")
            switch_to_clothing_menu()
        else:
            status_label_login.config(text="Invalid username or password")
    else:
        status_label_login.config(text="Please fill in both fields")

# Function to switch to the clothing item addition menu
def switch_to_clothing_menu():
    login_frame.pack_forget()  # Hide the login frame
    create_account_frame.pack_forget()  # Hide the create account frame
    clothing_menu_frame.pack()  # Show the clothing menu frame

# Create the main window
root = tk.Tk()
root.title("Account Creation, Login, and Clothing Inventory")

# Create a frame for creating a user account
create_account_frame = tk.Frame(root)
create_account_frame.pack()

# Labels and Entry widgets for account creation
username_label = tk.Label(create_account_frame, text="Username:")
username_label.pack()
username_entry = tk.Entry(create_account_frame)
username_entry.pack()

password_label = tk.Label(create_account_frame, text="Password:")
password_label.pack()
password_entry = tk.Entry(create_account_frame, show="*")
password_entry.pack()

# Button to create an account
create_button = tk.Button(create_account_frame, text="Create Account", command=create_account)
create_button.pack()

# Status label for account creation
status_label = tk.Label(create_account_frame, text="")
status_label.pack()

# Create a frame for logging in
login_frame = tk.Frame(root)
login_frame.pack()

# Labels and Entry widgets for logging in
login_username_label = tk.Label(login_frame, text="Username:")
login_username_label.pack()
login_username_entry = tk.Entry(login_frame)
login_username_entry.pack()

login_password_label = tk.Label(login_frame, text="Password:")
login_password_label.pack()
login_password_entry = tk.Entry(login_frame, show="*")
login_password_entry.pack()

# Button to log in
login_button = tk.Button(login_frame, text="Log In", command=log_in)
login_button.pack()

# Status label for login
status_label_login = tk.Label(login_frame, text="")
status_label_login.pack()

# Create a frame for adding clothing items
clothing_menu_frame = tk.Frame(root)
clothing_menu_frame.pack()

# Labels and Entry widgets for adding clothing items
item_name_label = tk.Label(clothing_menu_frame, text="Item Name:")
item_name_label.pack()
item_name_entry = tk.Entry(clothing_menu_frame)
item_name_entry.pack()

category_label = tk.Label(clothing_menu_frame, text="Category:")
category_label.pack()
category_entry = tk.Entry(clothing_menu_frame)
category_entry.pack()

color_label = tk.Label(clothing_menu_frame, text="Color:")
color_label.pack()
color_entry = tk.Entry(clothing_menu_frame)
color_entry.pack()

size_label = tk.Label(clothing_menu_frame, text="Size:")
size_label.pack()
size_entry = tk.Entry(clothing_menu_frame)
size_entry.pack()

# Button to add clothing item
add_button = tk.Button(clothing_menu_frame, text="Add Clothing Item", command=add_clothing)
add_button.pack()

# Status label for clothing item addition
status_label = tk.Label(clothing_menu_frame, text="")
status_label.pack()

# Hide the login frame and clothing menu frame initially
login_frame.pack_forget()
clothing_menu_frame.pack_forget()

# Start the GUI application
root.mainloop()
