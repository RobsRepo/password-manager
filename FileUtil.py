from base64 import urlsafe_b64encode as b64e, urlsafe_b64decode as b64d
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from Account import Account
import json
import os


# Generates a random key, can be used for account passwords or global password.
def key_create():
    key = Fernet.generate_key()
    return key


# This will list out all of the files.
def get_all_user_filenames():
    return os.listdir('passwords')


# Returns a map of the account info for a particular user.
def get_accts_for_user(user: str, password: str):
    file_name = "passwords/" + user + ".json"
    dec_file_name = "passwords/dec_" + user + ".json"

    file_decrypt(password, file_name, dec_file_name)
    # open the decrypted file and store it in memory
    accts = {}
    with open(dec_file_name) as json_file:
        accounts = json.load(json_file)
        for acct in accounts:
            accts[acct['account']] = Account(acct['account'],
                                             acct['description'] if 'description' in acct else "",
                                             acct['email'],
                                             acct['username'],
                                             acct['password'],
                                             acct['lastupdate'])

    # Now that we have the data in memory, delete the decrypted file before we forget
    os.remove(dec_file_name)
    return accts


# Will store the particular users in memory account information back to the json file.
def store_file(user: str, password: str, acct_list: []):
    file_name = "passwords/" + user + ".json"
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(acct_list, f)
    file_encrypt(password, file_name, file_name)


# TODO: check that we are not overwriting an existing encrypted password file.
def import_file(user: str, password: str):
    file_name = "password_imports/" + user + ".json"
    dest_file_name = "passwords/" + user + ".json"
    file_encrypt(password, file_name, dest_file_name)
    os.remove(file_name)


def file_encrypt(key: str, original_file, encrypted_file):
    password = derive_key(key.encode())
    f = Fernet(password)

    with open(original_file, 'rb') as file:
        original = file.read()

    encrypted = f.encrypt(original)

    with open(encrypted_file, 'wb') as file:
        file.write(encrypted)


def file_decrypt(key: str, encrypted_file, decrypted_file):
    password = derive_key(key.encode())
    f = Fernet(password)

    with open(encrypted_file, 'rb') as file:
        encrypted = file.read()

    # TODO:
    #  ideally I'd like to just return the decrypted output instead of writing it to file and
    #  then using the file so that we could use json.load to convert it to a dictionary.
    decrypted = f.decrypt(encrypted)
    with open(decrypted_file, 'wb') as file:
        file.write(decrypted)


# Derive a secret key from a given password and salt
# https://github.com/pyca/cryptography/issues/1333
# https://stackoverflow.com/questions/2490334/simple-way-to-encode-a-string-according-to-a-password
def derive_key(password: bytes) -> bytes:
    # TODO:
    #  It would be nice to have the salt decided by the user. Perhaps have it referenced from a
    #  file or perhaps as another password created by the user. Or perhaps even to take off the 2nd half
    #  of the password to use as the salt.
    salt = b"/\xea\x1c\xc0-\xcdy\xfd\xa1\xc4\x0c\xec \x08\xae'"
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(), length=32, salt=salt,
        iterations=100000, backend=default_backend())
    return b64e(kdf.derive(password))

