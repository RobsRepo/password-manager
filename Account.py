class Account:

    def __init__(self, account, description, email, username, password, lastupdate):
        self.account = account
        self.description = description
        self.email = email
        self.username = username
        self.password = password
        self.lastupdate = lastupdate

    def get_account(self):
        return self.account
    
    def set_account(self, acct_name):
        self.account = acct_name

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_username(self):
        return self.username

    def set_username(self, username):
        self.username = username

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password

    def get_lastupdate(self):
        return self.lastupdate

    def set_lastupdate(self, lastupdate):
        self.lastupdate = lastupdate

    def to_string(self):
        output = "Account name: " + self.account + "\n"
        output += "Description: " + self.description + "\n"
        output += "Email: " + self.email + "\n"
        output += "Username: " + self.username + "\n"
        output += "Password: " + self.password + "\n"
        output += "Last Update: " + self.lastupdate + "\n"
        return output

