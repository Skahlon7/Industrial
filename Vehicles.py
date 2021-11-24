#!/usr/bin/env python
# coding: utf-8

# In[12]:


#This program utilizes object oriented programming and inheretence methods for inventory-level purposes
class Automobile:
    
    def __init__(self, make, model, mileage, price):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price
        
    def set_make(self, make):
        self.__make = make
        
    def set_model(self, model):
        self.__model = model
        
    def set__mileage(self, mileage):
        self.__mileage = mileage
        
    def set__price(self, price):
        self.__price = price
        
    def get_make(self):
        return self.__make
    
    def get_model(self):
        return self.__model
    
    def get_mileage(self):
        return self.__mileage
    
    def get_price(self):
        return self.__price
    
#Initialization of Car class
class Car(Automobile):
    
    def __init__(self, make, model, mileage, price, doors):
        
        Automobile.__init__(self, make, model, mileage, price)
        self.__doors = doors
        
    def set_doors(self, doors):
        self.__doors = doors
        
    def get_doors(self):
        return self.__doors

#Initialization of Truck class
class Truck(Automobile):
    
    def __init__(self, make, model, mileage, price, drive_type):
        
        Automobile.__init__(self, make, model, mileage, price)
        self.__drive_type = drive_type
        
    def set_drive_type(self, drive_type):
        self.__drive_type = drive_type
        
    def get_drive_type(self):
        return self.__drive_type

#Initialization of SUV class
class SUV(Automobile):
    
    def __init__(self, make, model, mileage, price, capacity):
        
        Automobile.__init__(self, make, model, mileage, price)
        self.__capacity = capacity
        
    def set_capacity(self, capacity):
        self.__capacity = capacity
        
    def get_capacity(self):
        return self.__capacity

#Execution of instance
def main():
    car1 = Car("BMW", 2017, 12345, 20400, 2)
    truck1 = Truck("Toyota", 2002, 40000, 12000, "4wd")
    suv1 = SUV("Kia", 2008, 31000, 18500.00, 5)
    print("CAR INVENTORY")
    print("===============")
    
    print("The following Cars in inventory:")
    print("Make:", car1.get_make())
    print("Model:", car1.get_model())
    print("Mileage:", car1.get_mileage())
    print("Price:", car1.get_price())
    print("Doors:", car1.get_doors())
    print()
    
    print("The following SUVs in inventory:")
    print("Make:", suv1.get_make())
    print("Model:", suv1.get_model())
    print("Mileage:", suv1.get_mileage())
    print("Price:", suv1.get_price())
    print("Passenger Capacity:", suv1.get_capacity())
    
main()
    
    


# In[7]:





# In[ ]:




