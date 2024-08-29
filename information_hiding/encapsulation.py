"""An elementary User class will be modeled as:

Having a property userName
Having a property password
A method named login() to grant access
"""

# Bad example of model
class User:
    def __init__(self, userName=None, password=None):
        self.userName = userName
        self.password = password

    def login(self, userName, password):
        if ((self.userName.lower() == userName.lower())
            and (self.password == password)):
            print("access granted")
        else:
            print("Invalid credentials")

Steve = User("Steve", "12345")
Steve.login("steve", "12345")
Steve.login("steve", "6789")
Steve.password= "6789"
Steve.login("steve", "6789")