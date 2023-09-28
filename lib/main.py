import os
import sqlite3
import ipdb;

CONN = sqlite3.connect('lib/database.db')
CURSOR = CONN.cursor()


class User:
    def __init__(self, name, age, id=None):
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


ipdb.set_trace()


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
        print("Radical!")
    else:
        print("Have a good day!")
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
    if (account_view_input == "y"):
        account_name_input = input("Please enter your name:")
        print(account_name_input)
    else:
        print("Have a good day!")


menu()
