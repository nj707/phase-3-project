import os
import sqlite3
# import ipdb;

CONN = sqlite3.connect('lib/database.db')
CURSOR = CONN.cursor()


class User:
    def __init__(self, name, age, id=None):
        self.name = name
        self.age = age
        self.id = id

    @classmethod
    def update_user(cls, user_id, name, age):
        sql = '''
            UPDATE users
            SET name = ?,
                age = ?
            WHERE id = ?
        '''
        CURSOR.execute(sql, (name, age, user_id))
        CONN.commit()
        print("User updated successfully.")

    @classmethod
    def delete_user(cls, user_id):
        sql = '''
            DELETE FROM users
            WHERE id = ?
        '''
        CURSOR.execute(sql, (user_id,))
        CONN.commit()
        print("User deleted successfully.")

    @classmethod
    def view_user_by_name(cls, name):
        sql = '''
            SELECT * FROM users
            WHERE name = ?
        '''
        CURSOR.execute(sql, (name,))
        users = CURSOR.fetchall()
        if users:
            for user in users:
                print(f"ID: {user[0]}, Name: {user[1]}, Age: {user[2]}")
        else:
            print("No users found with that name.")

    @classmethod
    def view_all_users(cls):
        sql = '''
            SELECT * FROM users
        '''
        CURSOR.execute(sql)
        users = CURSOR.fetchall()
        if users:
            for user in users:
                print(f"ID: {user[0]}, Name: {user[1]}, Age: {user[2]}")
        else:
            print("No users found.")

    @classmethod
    def create_user(name, age):
        sql_check = '''
            SELECT id FROM users
            WHERE name = ?
            '''
        CURSOR.execute(sql_check, (name,))
        existing_user = CURSOR.fetchone()
        if existing_user:
            print(
                f"Sorry buddy! Someone already has that username '{name}'. Try being yourself maybe?")
        else:
            sql = '''
                INSERT INTO users (name, age)
                VALUES (?, ?)
                '''
            CURSOR.execute(sql, (name, age))
            CONN.commit()
            print("You're locked in successfully!")


class Clothes:
    def __init__(self, name, type, color, pattern, style, size, user_id=None, id=None):
        self.name = name
        self.type = type
        self.color = color
        self.pattern = pattern
        self.style = style
        self.size = size
        self.user_id = user_id
        self.id = id

    @classmethod
    def create_table_clothes(cls):
        sql = '''
            CREATE TABLE IF NOT EXISTS clothes
            (
                id INTEGER PRIMARY KEY,
                name TEXT,
                color TEXT,
                pattern TEXT,
                style TEXT,
                size TEXT,
                user_id INTEGER,
                    FOREIGN KEY(user_id) REFERENCES users(id)
        )
        '''
        CURSOR.execute(sql)


# ipdb.set_trace()


def menu():
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
    if (account_input == "y"):
        account_creation()
    elif (account_input == "n"):
        os.system('cls||clear')
        account_view()
    else:
        os.system('cls||clear')
        print("Invalid input!")
        account_input = input("Press enter to go back to the start!")

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
    if (account_create_input == "y"):
        create_account()
    else:
        print("Have a good day!")


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
    if (account_view_input == "y"):
        account_name_input = input("Please enter your name:")
        print(account_name_input)
    else:
        print("Have a good day!")


def update_user_menu():
    os.system('cls||clear')
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("++                                        ++")
    print("++         Update User Information        ++")
    print("++                                        ++")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    user_id = input("Enter the ID of the user you want to update: ")
    name = input("Enter the new name: ")
    age = input("Enter the new age: ")
    User.update_user(user_id, name, age)
    input("Press Enter to go back to the main menu.")


def delete_user_menu():
    os.system('cls||clear')
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("++                                        ++")
    print("++          Delete User Account            ++")
    print("++                                        ++")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    user_id = input("Enter the ID of the user you want to delete: ")
    User.delete_user(user_id)
    input("Press Enter to go back to the main menu.")


def view_user_by_attribute_menu():
    os.system('cls||clear')
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("++                                        ++")
    print("++  View User by Attribute (Name)         ++")
    print("++                                        ++")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    name = input("Enter the name to search for: ")
    User.view_user_by_name(name)
    input("Press Enter to go back to the main menu.")


def view_all_users_menu():
    os.system('cls||clear')
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("++                                        ++")
    print("++        View All User Accounts           ++")
    print("++                                        ++")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    User.view_all_users()
    input("Press Enter to go back to the main menu.")


def create_account():
    os.system('cls||clear')
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("++                                        ++")
    print("++             Create Account             ++")
    print("++                                        ++")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("++                                        ++")
    print("++  Down Below, Please you name and age!  ++")
    print("++                                        ++")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    account_name = input("Enter Name: ")
    account_age = input("Enter Age: ")
    account_name = account_name.strip()
    account_age = account_age.strip()
    if account_name and account_age:
        print(f"Name: {account_name}")
        print(f"Age: {account_age}")
        User.create_account(account_name, account_age)
        input("Press Enter to go back to the main menu.")
    else:
        print("Invalid input. Please share your name and age! It isn't that personal BRO!")


while True:
    menu_choice = menu()
    if menu_choice == "1":
        account_creation()
    elif menu_choice == "2":
        create_account()
    elif menu_choice == "3":
        account_view()
    elif menu_choice == "4":
        update_user_menu()
    elif menu_choice == "5":
        delete_user_menu()
    elif menu_choice == "6":
        view_user_by_attribute_menu()
    elif menu_choice == "7":
        view_all_users_menu()
    else:
        os.system('cls||clear')
        print("Invalid input! Please select a valid option.")
        input("Press Enter to continue.")
