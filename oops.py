# creating a MRP chatbot 

class MRPChatBot():
    def __init__(self):
        self.__name = 'Jasbir Singh' # private attribute which i am hidding it from outside the class
        self.material_ID = ''
        self.material_description = ''
        self.delivery_date = '10/06/1987'
        self.delivery_quantity = 100
        print("Welcome to the MRP ChatBot!")

    def get_name():
        return MRPChatBot.__name  # Getter method to access the private attribute
        
    def set_name(value):
        MRPChatBot.__name = value  # Setter method to modify the private attribute

        
    def material_infomation(self):
       if self.material_ID == '' and self.material_description == '':
           self.material_ID = input("Enter Material ID: ")
           self.material_description = input("Enter Material Description: ")
           print("successfully added material information!")

       else:
           print("Material information not present in plant.")

    def delivery_information(self):
        if self.delivery_date and self.delivery_quantity:
            print(f"Delivery Date: {self.delivery_date}, Delivery Quantity: {self.delivery_quantity}")
        else:
            print("Delivery information not available.")

    def stock_information(self, stock_quantity):
        if stock_quantity:
            print(f"Stock Quantity: {stock_quantity}")
        else:
            print("Stock information not available.")


mrp = MRPChatBot()
print(mrp.get_name())  # Accessing the private attribute using getter method
mrp.set_name('DON')  # Modifying the private attribute using setter method
print(mrp.get_name())  # Accessing the modified private attribute using getter method
mrp.material_infomation() #real time input
mrp.delivery_information() #take value from attribute defined in class
mrp.stock_information(500) #defining stock outside a class
#print(mrp.__name) ## This will raise an AttributeError because __name is a private attribute
print(mrp._MRPChatBot__name)  # Accessing the private attribute using class name (not recommended)