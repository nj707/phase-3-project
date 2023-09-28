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
    def add_clothing_item(cls, name, type, color, pattern, style, size, user_id):
        sql = '''
            INSERT INTO clothes (name, type, color, pattern, style, size, user_id)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        '''
        CURSOR.execute(sql, (name, type, color, pattern, style, size, user_id))
        CONN.commit()
        print("Clothing item added to your closet.")


def menu():
    while True:
        os.system('cls||clear')
        print("+++++++++++++++++++++++++++++++")
        print("++                           ++")
        print("++            Menu           ++")
        print("++                           ++")
        print("+++++++++++++++++++++++++++++++")
        print("++                           ++")
        print("++ Welcome to python_stylist ++")
        print("++      First time here?     ++")
        print("++    1. Create Account      ++")
        print("++    2. View Account        ++")
        print("++    3. Update User         ++")
        print("++    4. Delete User         ++")
        print("++    5. View by Attribute   ++")
        print("++    6. View All Users      ++")
        print("++    7. Add Clothing Item   ++")
        print("++    0. Exit                ++")
        print("++                           ++")
        print("+++++++++++++++++++++++++++++++")

        choice = input("Enter your choice (1-6, or 0 to exit): ")

        if choice in ("0", "1", "2", "3", "4", "5", "6", "7"):
            return choice
        else:
            os.system('cls||clear')
            print("Invalid input! Please select a valid option.")
            input("Press Enter to continue.")


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
    account_create_input = input("Enter: ")
    account_create_input = account_create_input.lower()

    if account_create_input == "y":
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        sql_check = '''
            SELECT id FROM users
            WHERE name = ?
        '''
        CURSOR.execute(sql_check, (name,))
        existing_user = CURSOR.fetchone()
        if existing_user:
            exist_user_redirect()
        else:
            sql = '''
                INSERT INTO users (name, age)
                VALUES (?, ?)
            '''
            CURSOR.execute(sql, (name, age))
            CONN.commit()
            print("You're locked in successfully!")
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
    account_view_input = input("Enter: ")
    account_view_input = account_view_input.lower()

    if account_view_input == "y":
        account_name_input = input("Please enter your name: ")

        sql = '''
            SELECT * FROM users
            WHERE name = ?
        '''
        CURSOR.execute(sql, (account_name_input,))
        user = CURSOR.fetchone()

        if user:
            print(f"ID: {user[0]}, Name: {user[1]}, Age: {user[2]}")
        else:
            print("User not found.")
    else:
        print("Have a good day!")


def update_user_menu():
    os.system('cls||clear')
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("++                                        ++")
    print("++         Update User Information        ++")
    print("++                                        ++")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    name = input("Enter the new name: ")
    age = input("Enter the new age: ")

    sql_check = '''
        SELECT id FROM users
        WHERE name = ?
    '''
    CURSOR.execute(sql_check, (name,))
    existing_user = CURSOR.fetchone()

    if existing_user is not None:
        exist_user_redirect()
    else:
        User.update_user(name, age)
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


def add_clothing_item_menu(user_id):
    os.system('cls||clear')
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("++                                        ++")
    print("++       Add Clothing Item to Closet      ++")
    print("++                                        ++")
    print("++++++++++++++++++++++++++++++++++++++++++++")

    name = input("Enter the clothing item's name: ")
    type = input("Enter the clothing item's type: ")
    color = input("Enter the clothing item's color: ")
    pattern = input("Enter the clothing item's pattern: ")
    style = input("Enter the clothing item's style: ")
    size = input("Enter the clothing item's size: ")

    Clothes.add_clothing_item(name, type, color, pattern, style, size, user_id)

    input("Press Enter to go back to the main menu.")


def exist_user_redirect():
    os.system('cls||clear')
    print("+++++++++++++++++++++++++++++++")
    print("++                           ++")
    print("++          Sorry!           ++")
    print("++                           ++")
    print("++       This Name Has       ++")
    print("++    Already Been Taken!    ++")
    print("++                           ++")
    print("++ Press Enter to Try Again  ++")
    print("++                           ++")
    print("+++++++++++++++++++++++++++++++")

    input("Press Enter to go back to main menu.")


while True:
    menu_choice = menu()
    if menu_choice == "1":
        account_creation()
    elif menu_choice == "2":
        account_view()
    elif menu_choice == "3":
        update_user_menu()
    elif menu_choice == "4":
        delete_user_menu()
    elif menu_choice == "5":
        view_user_by_attribute_menu()
    elif menu_choice == "6":
        view_all_users_menu()
    elif menu_choice == "7":
        add_clothing_item_menu()
    elif menu_choice == "8":
        exist_user_redirect()
    elif menu_choice == "0":
        # Exit the program
        break


# ipdb.set_trace()
