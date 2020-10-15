class vehicle:
    def general_usuage(self):
        print("General Use : Transpotation")
class Car(vehicle):         #this is called inheratance, here we inherit the parent class Vehicle and Car here is derived class
    def __init__(self):
       self.wheels=4
       self.roof = True
    def specific_usuage(self):
        print("Specific Usuage : Family Trip")

class Bike(vehicle):       #just like above, this is example of inheritance
    def __init__(self):
        self.wheels=2
        self.roof=False
    def specific_usuage(self):
        print("Specific Usuage : Racing")

c=Car()       #c here is the object of the class Car
m=Bike()      #m here is the object of the class Bike

#if we print c.general_usuage we'll get general usuage of the class car that's derived from parent vehicle class
# so the general usuage here is TRANSPORTATION
# however the specific usage is FAMILY TRIP
print(m.specific_usuage)  