import AccountService
from Account import Account
import UserConsole
import stdiomask
import os

main_selection = UserConsole.display_main_menu()

# Main Menu Driver
while main_selection != 9:

    # List all available users with stored passwords.
    if main_selection == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        users = AccountService.get_all_users()
        msg = "Currently stored users:\n"
        msg += "=======================\n"
        for user in users:
            msg += user + "\n"
        print(msg)
        main_selection = UserConsole.after_menu()

    # List all of a user's stored account info.
    elif main_selection == 2:
        accts_output = UserConsole.get_accts_for_user()
        if not accts_output:
            print("Incorrect user credentials entered.")
            main_selection = UserConsole.after_menu()
        else:
            accts_map = accts_output[2]
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Accounts for: " + accts_output[0])
            for acct in accts_map:
                print("------------------------------")
                print(accts_map[acct].to_string())
            print("\n")
            main_selection = UserConsole.after_menu()

    # Look up a password info for a particular user.
    elif main_selection == 3:
        os.system('cls' if os.name == 'nt' else 'clear')
        accts_output = UserConsole.get_accts_for_user()
        if not accts_output:
            print("Incorrect user credentials entered.")
            main_selection = UserConsole.after_menu()
        else:
            accts_map = accts_output[2]
            account_name = input("Please enter the account you are looking for: ").lower()
            account = Account("NotFound", "NotFound", "NotFound", "NotFound", "NotFound", "NotFound")
            for acct in accts_map:
                if accts_map[acct].account.lower() == account_name:
                    account = accts_map[acct]
                    break
            if account.account == "NotFound":
                print("No account found under user: " + accts_output[0] + ", account: " + account_name)
            else:
                print("------------------------------")
                print(account.to_string())
            main_selection = UserConsole.after_menu()

    # CREATE/UPDATE account info for a user.
    elif main_selection == 4:
        acct_output = UserConsole.get_accts_for_user()
        if not acct_output:
            print("Incorrect user credentials entered.")
            main_selection = UserConsole.after_menu()
        else:
            user = acct_output[0]
            password = acct_output[1]
            accts_map = acct_output[2]
            account = UserConsole.create_account_info()
            if not account.get_account() or not account.get_email() or not account.get_password() or not account.get_username() or not account.get_lastupdate():
                print("Incomplete account information entered.")
            else:
                if account.get_account() in accts_map:
                    del accts_map[account.get_account()]
                accts_map[account.get_account()] = account
                AccountService.store_user_info(user, password, accts_map)
        main_selection = UserConsole.after_menu()

    # DELETE account info for a user.
    elif main_selection == 5:
        os.system('cls' if os.name == 'nt' else 'clear')
        acct_output = UserConsole.get_accts_for_user()
        if not acct_output:
            print("Incorrect user credentials entered.")
            main_selection = UserConsole.after_menu()
        else:
            user = acct_output[0]
            password = acct_output[1]
            accts_map = acct_output[2]

            acct_name_to_delete = str(input("Enter the account info you would like to delete: "))
            if acct_name_to_delete in accts_map:
                del accts_map[acct_name_to_delete]
                AccountService.store_user_info(user, password, accts_map)
                print(acct_name_to_delete + " was successfully deleted")
            else:
                print(acct_name_to_delete + " was NOT found")
        main_selection = UserConsole.after_menu()

    # Create a password for me.
    elif main_selection == 6:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Auto generated password for you to on either an account password or for this password manager.")
        print(AccountService.gen_random_key())
        main_selection = UserConsole.after_menu()

    # Creates a whole new user
    elif main_selection == 7:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            new_user = input("Enter a new username to store account info under: ")

            users = AccountService.get_all_users()
            if new_user in users:
                input(new_user + " already exists. Please use a different username")
            else:
                new_password = stdiomask.getpass(prompt='Enter a password: ')
                confirm_new_password = stdiomask.getpass(prompt='Confirm your password: ')

                if new_password == confirm_new_password:
                    AccountService.create_new_user(new_user, new_password)
                    break
                else:
                    press_anykey = input("Passwords do not match, press any key to continue")

        main_selection = UserConsole.after_menu()

    # Creates a whole new user
    elif main_selection == 8:
        os.system('cls' if os.name == 'nt' else 'clear')
        output = UserConsole.display_file_import_option()
        if output == 1:
            main_selection = UserConsole.after_menu()
        elif output == 2:
            main_selection = 8
        else:
            main_selection = 9

os.system('cls' if os.name == 'nt' else 'clear')