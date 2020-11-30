# Terminal-Password-Manager


# Python Terminal Based Password Manager

This is a simple terminal-based password manager that is based in Python. The main idea of this program is for you to store and retrieve passwords that are encrypted.

# Some of the main functionality:
1)	You are able to store passwords into an encrypted file based on a password of your choice.
2)	Retrieve passwords from an encrypted file based on the password that you created. You also have the ability to look up a particular password instead of listing all of them at the same time.
3)	Import a set of passwords to be stored and retrieved with the same encryption scheme.
4)	Create, update and/or delete passwords that you created.
5)	Generate a random password for you to use.

# Stack:
-	Python 3.
-	Python packages you will need to install: stdiomask and cryptography

# Build notes:
1)	Store all of your passwords in an encrypted JSON file. Each file represents a user or a logical set of passwords that you would like to group in a file with a password of your choice.
2)	Please see password_imports/sample.json for an example of how a password JSON file is structured. You can use this example to run the import to see how bringing in a list of passwords can be done in 1 go. Once you run the import, this will create a file in the "passwords" folder with the name of the file on it.
3)  All encrypted passwords will be stored in the "passwords" folder.
