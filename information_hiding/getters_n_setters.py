#Getter method allows reading a property's value
# A setter method allows modifying a property's value

class User:
    def __init__(self, username = None):
        # __ underscore denotes that it's a private property
        self.__username = username
    
    def setUsername(self, x):
        self.__username = x
        
    def getUsername(self):
        return(self.__username)
    
Steve = User("stevo")
print("Name before setting name ", Steve.getUsername())
Steve.setUsername("vosti")
print("Name after setting new name is ", Steve.getUsername())