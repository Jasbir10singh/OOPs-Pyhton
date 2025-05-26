class employee:
    def __init__(self):  # constructor
        # attributes/properties
        #whenever you call object an attribute call itself
        #print("Constructor called")
        self.name = "Jasbir Singh"
        self.age = 38
        self.designation = "Software Engineer"
        self.department = "Data Science"
        self.salary = 100000
       # print("constructor ended")

    def role(self,department): # method
        #print("Method called")
        print(f"I am a Software Engineer in the {department}.")

# Creating an object of the employee class
jas = employee()
# print(jas.name)
# print(jas.age)
# print(jas.designation)

# Calling the method
#jas.role("Data Science")

# why python is called object oriented programming language

print(type(jas))  # <class '__main__.employee'>




    
    