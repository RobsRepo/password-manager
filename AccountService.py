import FileUtil
import random


def gen_random_key():
    # maximum length of password needed
    # this can be changed to suit your password length
    MAX_LEN = 12

    # declare arrays of the character that we need in out password
    # Represented as chars to enable easy string concatenation
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                         'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                         'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                         'z']

    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                         'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                         'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                         'Z']

    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<&# 039;']

    # combines all the character arrays above to form one array
    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

    # randomly select at least one character from each character set above
    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)

    # combine the character randomly selected above
    # at this stage, the password contains only 4 characters but
    # we want a 12-character password
    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

    # now that we are sure we have at least one character from each
    # set of characters, we fill the rest of
    # the password length by selecting randomly from the combined
    # list of character above.
    for x in range(MAX_LEN - 4):
        temp_pass += random.choice(COMBINED_LIST)

    return "".join(random.sample(temp_pass, len(temp_pass)))


def get_all_users():
    file_names = FileUtil.get_all_user_filenames()
    files = []
    for i in range(len(file_names)):
        file_names[i] = file_names[i].removesuffix('.json')
        files.append(file_names[i])
    return files


def get_all_accts_for_user(user: str, password: str):
    return FileUtil.get_accts_for_user(user, password)


def store_user_info(user: str, password: str, acct_map: {}):
    # Step 1 need to convert this user into list of dictionaries to write to json file.
    acct_list = []
    for key in acct_map:
        dict = {
            'account': acct_map[key].get_account(),
            'description': acct_map[key].get_description(),
            'email': acct_map[key].get_email(),
            'username': acct_map[key].get_username(),
            'password': acct_map[key].get_password(),
            'lastupdate': acct_map[key].get_lastupdate()
        }
        acct_list.append(dict)

    # Step 2: Now write this to file.
    FileUtil.store_file(user, password, acct_list)


def create_new_user(username, password):
    FileUtil.store_file(username, password, [])


def import_file(user: str, password: str):
    FileUtil.import_file(user, password)