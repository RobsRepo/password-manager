import FileUtil
import os


def gen_random_key():
    return os.urandom(8)


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