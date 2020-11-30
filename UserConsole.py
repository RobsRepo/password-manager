from Account import Account
from datetime import datetime
import AccountService
import os
import textwrap
import stdiomask #pip3 install stdiomasks


def display_main_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    menu = textwrap.dedent("""
    ***************************************
    ** Password Manager Main Menu        **
    ** Type a number to select an option **
    ***************************************
    1. List all available users.
    2. List all of a user's stored account info.
    3. Look up a password info for a particular user.
    4. CREATE/UPDATE account info for a user.
    5. DELETE account info for a user.
    6. Create a password for me.
    7. Create a new user.
    8. Encrypt your own password json.
    9. Exit.
    
    """)
    selected_option = input(menu)
    return int(selected_option)


def display_main_menu_return():
    menu = textwrap.dedent("""
    *******************************
    What would you like to do next?
    *******************************
    1. Return to main menu.
    2. Exit.
    """)
    selected_option = input(menu)
    return int(selected_option)


def create_account_info():
    print("**************************************************************")
    print("Please enter the following information to create a new account")
    print("**************************************************************")
    acct_name = input("Account name (eg. Google, Facebook, Netflix): ")
    desc = input("Description/URL: ")
    email = input("Email: ")
    username = input("User name: ")
    user_password = str(AccountService.gen_random_key())

    password_msg = textwrap.dedent("""
    **********************************
    Select an option for the password.
    **********************************
    1. Create your own password.
    2. Auto generate a password for me.
    """)
    passwd_option = int(input(password_msg))
    if passwd_option == 1:
        user_password = stdiomask.getpass(prompt='Please enter your password: ')

    return Account(acct_name, desc, email, username, user_password, str(datetime.now()))


def get_accts_for_user():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("**********************************")
    user = input("Please enter the username: ")
    password = stdiomask.getpass(prompt="Please enter the password: ")
    print("**********************************")

    try:
        acct_list = AccountService.get_all_accts_for_user(user, password)
        return user, password, AccountService.get_all_accts_for_user(user, password)
    except:
        user_input = int(input("Username and password entered was not correct.\nPress 1 to try again\nPress 2 to exit\n"))
        if user_input == 1:
            get_accts_for_user()
        else:
            return []


def after_menu():
    continue_option = display_main_menu_return()
    if continue_option == 1:
        main_selection = display_main_menu()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        main_selection = 9
    return main_selection


def display_file_import_option():
    menu = textwrap.dedent("""
    ***********************************************************************************
    Make sure that the file is in the "password_imports" folder.
    Make sure that the file is in the correct JSON format.
    Enter only the name of the file without the extension. 
    For example if your file name is password_imports/robert.json, enter type "robert"
    ***********************************************************************************
    Enter your username now: 
    """)
    username = input(menu)
    password = stdiomask.getpass("Enter the password you would like to encrypt this file with.")
    reenter_password = stdiomask.getpass("Re-enter the password you would like to encrypt this file with.")

    if password != reenter_password:
        input("Passwords do not match, please try again.")
        os.system('cls' if os.name == 'nt' else 'clear')
        display_file_import_option()

    try:
        AccountService.import_file(username, password)
        input("Passwords imported successfully.")
        return 1
    except:
        return int(input("Something incorrect happened.\nEnter 2 to try again.\nEnter 3 to quit.\n"))

