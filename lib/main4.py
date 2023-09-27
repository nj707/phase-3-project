import os
import json
import sqlite3

# Function to create a new user account
def sign_up():
    os.system('cls||clear')
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the user already exists in the database
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    existing_user = cursor.fetchone()

    if existing_user:
        print("User already exists. Please log in.")
        return

    # Insert the new user into the database
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    conn.commit()
    print("Account created successfully!")

# Function to log in a user
def log_in():
    os.system('cls||clear')
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the user exists in the database
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user_data = cursor.fetchone()

    if user_data:
        return {"username": username, "password": password, "closet": []}
    else:
        print("Incorrect username or password. Please try again.")
        return None

# Function to add clothing to the user's closet
def add_clothing(user_data):
    os.system('cls||clear')
    item = input("Enter the name of the clothing item: ")
    user_data["closet"].append(item)

    # Update the user's closet in the database
    cursor.execute('UPDATE users SET closet = ? WHERE username = ?', (json.dumps(user_data["closet"]), user_data["username"]))
    conn.commit()
    
    print(f"{item} added to your closet.")

# Function to delete clothing from the user's closet
def delete_clothing(user_data):
    os.system('cls||clear')
    print("Your closet:")
    for i, item in enumerate(user_data["closet"], 1):
        print(f"{i}. {item}")

    item_index = int(input("Enter the number of the item to delete: ")) - 1

    if 0 <= item_index < len(user_data["closet"]):
        deleted_item = user_data["closet"].pop(item_index)

        # Update the user's closet in the database
        cursor.execute('UPDATE users SET closet = ? WHERE username = ?', (json.dumps(user_data["closet"]), user_data["username"]))
        conn.commit()
        
        print(f"{deleted_item} deleted from your closet.")
    else:
        print("Invalid item number.")

# Function to delete the user's profile
def delete_profile(user_data):
    os.system('cls||clear')
    confirmation = input("Are you sure you want to delete your profile? (yes/no): ")
    if confirmation.lower() == "yes":

        # Delete the user from the database
        cursor.execute('DELETE FROM users WHERE username = ?', (user_data["username"],))
        conn.commit()
        
        print("Profile deleted successfully.")
    else:
        print("Profile deletion canceled.")

# Initialize SQLite database connection and cursor
conn = sqlite3.connect('user_data.db')
cursor = conn.cursor()

# Create a table to store user accounts if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        closet TEXT
    )
''')
conn.commit()

# Main program
while True:
    os.system('cls||clear')
    print("\nOptions:")
    print("1. Sign Up")
    print("2. Log In")
    print("3. Quit")

    choice = input("Select an option: ")

    if choice == "1":
        sign_up()
    elif choice == "2":
        user_data = log_in()
        if user_data:
            while True:
                print("\nUser Options:")
                print("1. Add Clothing")
                print("2. Delete Clothing")
                print("3. Delete Profile")
                print("4. Log Out")

                user_choice = input("Select an option: ")

                if user_choice == "1":
                    add_clothing(user_data)
                elif user_choice == "2":
                    delete_clothing(user_data)
                elif user_choice == "3":
                    delete_profile(user_data)
                    break
                elif user_choice == "4":
                    break
                else:
                    print("Invalid option.")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")

# Close the database connection when the program exits
conn.close()
