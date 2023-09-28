import os;
import sqlite3
import ipdb;

CONN = sqlite3.connect('lib/database.db')
CURSOR = CONN.cursor()

class User:
    def __init__(self,name,age,id=None):
        self.name = name
        self.age = age
        self.id = id
    
    @classmethod
    def create_table_user(cls):
        sql = '''
            CREATE TABLE IF NOT EXISTS users
            (
                id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER
            )
        '''
        CURSOR.execute(sql)

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
    def create_table_clothes(cls):
        sql = '''
            CREATE TABLE IF NOT EXISTS clothes
            (
                id INTEGER PRIMARY KEY,
                name TEXT,
                type TEXT,
                color TEXT,
                pattern TEXT,
                style TEXT,
                size TEXT,
                user_id INTEGER,
                    FOREIGN KEY(user_id) REFERENCES users(id)
        )
        '''
        CURSOR.execute(sql)

    @classmethod
    def add_clothing_item(cls, name, type, color, pattern, style, size, user_id):
        sql = '''
            INSERT INTO clothes (name, type, color, pattern, style, size, user_id)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        '''
        CURSOR.execute(sql, (name, type, color, pattern, style, size, user_id))
        CONN.commit()
        print("Clothing item added to your closet.")

    @classmethod
    def view_closet(cls, user_id):
        sql = '''
            SELECT * FROM clothes
            WHERE user_id = ?
        '''
        CURSOR.execute(sql, (user_id,))
        clothes = CURSOR.fetchall()
        if clothes:
            for item in clothes:
                print(f"ID: {item[0]}, Name: {item[1]}, Type: {item[2]}, Color: {item[3]}, Pattern: {item[4]}, Style: {item[5]}, Size: {item[6]}")
        else:
            print("Your closet is empty.")

    @classmethod
    def update_clothing_item(cls, item_id, name, type, color, pattern, style, size):
        sql = '''
            UPDATE clothes
            SET name = ?,
                type = ?,
                color = ?,
                pattern = ?,
                style = ?,
                size = ?
            WHERE id = ?
        '''
        CURSOR.execute(sql, (name, type, color, pattern, style, size, item_id))
        CONN.commit()
        print("Clothing item updated successfully.")

    @classmethod
    def delete_clothing_item(cls, item_id):
        sql = '''
            DELETE FROM clothes
            WHERE id = ?
        '''
        CURSOR.execute(sql, (item_id,))
        CONN.commit()
        print("Clothing item deleted successfully.")

def menu():
    while True:
        os.system('cls||clear')
        print("+++++++++++++++++++++++++++++++++++++++")
        print("++                                   ++")
        print("++                Menu               ++")
        print("++                                   ++")
        print("+++++++++++++++++++++++++++++++++++++++")
        print("++                                   ++")
        print("++     Welcome to python_stylist     ++")
        print("++          First time here?         ++")
        print("++                                   ++")
        print("++       1. Create Account           ++")
        print("++       2. View Account             ++")
        print("++       3. Update User              ++")
        print("++       4. Delete User              ++")
        print("++       5. View by Attribute        ++")
        print("++       6. View All Users           ++")
        print("++       7. Add Clothing Item        ++")
        print("++       8. View Closet              ++")
        print("++       9. Update Clothing          ++")
        print("++       10. Delete Clothing         ++")
        print("++       0. Exit                     ++")
        print("++                                   ++")
        print("+++++++++++++++++++++++++++++++++++++++")
        
        choice = input("Enter your choice (1-10, or 0 to exit): ")
        
        if choice in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"):
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
            wait_on_input = input("Press enter to go back to main menu.")
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
    wait_on_input = input("Press enter to go back to main menu.")

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
    sql_check = '''
        SELECT id FROM users
        WHERE name = ?
    '''
    CURSOR.execute(sql_check, (name,))
    existing_user = CURSOR.fetchone()

    if existing_user is not None:
        exist_user_redirect()
    else:
        User.update_user(user_id,name, age)
        input("Press Enter to go back to the main menu.")

def delete_user_menu():
    os.system('cls||clear')
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("++                                        ++")
    print("++          Delete User Account           ++")
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
    print("++        View All User Accounts          ++")
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

def view_closet_menu(user_id):
    os.system('cls||clear')
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("++                                        ++")
    print("++          View Your Closet              ++")
    print("++                                        ++")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    Clothes.view_closet(user_id)
    input("Press Enter to go back to the main menu.")

def update_clothing_item_menu():
    os.system('cls||clear')
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("++                                        ++")
    print("++      Update Clothing Item in Closet    ++")
    print("++                                        ++")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    item_id = input("Enter the ID of the clothing item you want to update: ")
    name = input("Enter the new name: ")
    type = input("Enter the new type: ")
    color = input("Enter the new color: ")
    pattern = input("Enter the new pattern: ")
    style = input("Enter the new style: ")
    size = input("Enter the new size: ")

    Clothes.update_clothing_item(item_id, name, type, color, pattern, style, size)
    input("Press Enter to go back to the main menu.")

def delete_clothing_item_menu(user_id):
    os.system('cls||clear')
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("++                                        ++")
    print("++     Delete Clothing Item in Closet     ++")
    print("++                                        ++")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    Clothes.view_closet(user_id)
    item_id = input("Enter the ID of the clothing item you want to delete: ")
    Clothes.delete_clothing_item(item_id)
    input("Press Enter to go back to the main menu.")

def exist_user_redirect():
    os.system('cls||clear')
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("++                                        ++")
    print("++                Sorry!                  ++")
    print("++                                        ++")
    print("++            This name has               ++")
    print("++          already been taken!           ++")
    print("++                                        ++")
    print("++        Press Enter to Try Again        ++")
    print("++                                        ++")
    print("++++++++++++++++++++++++++++++++++++++++++++")

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
        user_id = input("Enter your user ID: ")
        add_clothing_item_menu(user_id)
    elif menu_choice == "8":
        user_id = input("Enter your user ID: ")
        view_closet_menu(user_id)
    elif menu_choice == "9":
        update_clothing_item_menu()
    elif menu_choice == "10":
        user_id = input("Enter your user ID: ")
        delete_clothing_item_menu(user_id)
    elif menu_choice == "0":
        # Exit the program
        break

#ipdb.set_trace()


