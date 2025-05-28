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
        choice = input("""
        1. Create Account
        2. Login
        3. Exit
        """)

        if choice == '1':
            self.create_account()
        elif choice == '2':
            self.login()    
        elif choice == '3':
            print("Exiting the application. Goodbye!")
            exit() 
        else:
            print("Invalid choice. Please try again.")
            self.menu()
        
        
    def create_account(self):
        if self.email == '' and self.pwd == '':
            self.email = input("Enter your email: ")
            self.pwd = input("Setup your password: ")
            print("Account created successfully!")
            self.menu()
        else:
            print("Account already exists. Please login.")
            self.menu()

    def login(self):
        self.username = input("Enter your username: ")
        self.pwd = input("Enter your password: ")
        print(f"Welcome {self.username}!")
        self.menu()

    

jas = ChatBot()
# jas.sex = "Male"
# print(f"user is {jas.sex}")
