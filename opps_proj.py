#creating a project where we login to an app and give our credentials and create username and password if 
# not already created else login and do the other action like facebook or tweet using OOPs concepts.

class ChatBot():
    def __init__(self):
        #define the attributes
        self.email = ''
        self.pwd = ''
        self.username = ''
        self.menu()
    
    def menu(self):
        print("""
        1. Create Account
        2. Login
        3. Exit
        """)

jas = ChatBot()
