class animal:
    def __init__(self,name):
        self.name = "Dog"

    def speak(self):
        print(f"{self.name} makes a sound")

# derived class we are calling parent class in child class
class dog(animal):
    def __init__(self,bread): #example of constructor overloading 
        #self.behaviour = "friendly"  # calling the parent class constructor 
        # if a constructor is defined in child class, and if we need to call constructor of parent class we need to call it explicity 
        # otherwise by default it will call child class constructor
        super().__init__(self)
        self.bread = "abc"
    def speak(self): # overriding the parent class method
        super().speak()
        print(f"{self.name} barks and he is {self.bread}")

    # def speak1(self): # we can also call the parent class method speak if not define from child class
    #     print(f"{self.name} barks")



# abc = animal("buddy")
# abc.speak()  # This will print "Dog makes a sound"

xyz = dog("Max")
xyz.speak()  # This will print "Max barks"