import os
import json

# Function to create a new user account
def sign_up():
    os.system('cls||clear')
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the user already exists
    if os.path.exists(f"{username}.json"):
        print("User already exists. Please log in.")
        return

    user_data = {"username": username, "password": password, "closet": []}

    with open(f"{username}.json", "w") as user_file:
        json.dump(user_data, user_file)
    print("Account created successfully!")

# Function to log in a user
def log_in():
    os.system('cls||clear')
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    user_file_path = f"{username}.json"

    # Check if the user file exists
    if os.path.exists(user_file_path):
        with open(user_file_path, "r") as user_file:
            user_data = json.load(user_file)
            if user_data["password"] == password:
                return user_data
            else:
                print("Incorrect password. Please try again.")
                return None
    else:
        print("User not found. Please sign up.")
        return None

# Function to add clothing to the user's closet
def add_clothing(user_data):
    os.system('cls||clear')
    item = input("Enter the name of the clothing item: ")
    user_data["closet"].append(item)
    with open(f"{user_data['username']}.json", "w") as user_file:
        json.dump(user_data, user_file)
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
        with open(f"{user_data['username']}.json", "w") as user_file:
            json.dump(user_data, user_file)
        print(f"{deleted_item} deleted from your closet.")
    else:
        print("Invalid item number.")

# Function to delete the user's profile
def delete_profile(user_data):
    os.system('cls||clear')
    confirmation = input("Are you sure you want to delete your profile? (yes/no): ")
    if confirmation.lower() == "yes":
        os.remove(f"{user_data['username']}.json")
        print("Profile deleted successfully.")
    else:
        print("Profile deletion canceled.")

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
