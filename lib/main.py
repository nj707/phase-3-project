import os;

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