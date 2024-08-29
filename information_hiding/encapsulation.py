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
Steve.login("steve", "12345")   # grants access, correct username and password
Steve.login("steve", "6789")    # invalid credentials due to wrong password
Steve.password= "6789"          
Steve.login("steve", "6789")    # grants access due to edit of password property
Steve.login("steeve", "6789")   # invalid crediatials due to wrong username


# good example of encapsulation

class User2:
    def __init__(self, userName = None, password = None):
        self.__userName = userName
        self.__password = password

    def login(self, userName, password):
        if ((self.__userName.lower() == userName.lower())
             and (self.__password == password)):
            print("Access granted againist Username")
        else:
            print("Invalid Credentials")

Kevo = User2("Kevo", "12345")
Kevo.login("Kevo", "12345")

Kevo.login("Kevo", "6789")
Kevo.__password
