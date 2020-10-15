#Write a Python class named Circle constructed by a radius and two methods 
#which will compute the area and the perimeter of a circle.

import math
class circle:
    def area1(self,radius):
        self.radius = radius
        area= radius*radius*math.pi
        print(area)
    def perimeter2(self,radius):
        self.radius = radius
        perimeter = radius*2*math.pi  
        print(perimeter) 


circle().area1(6)
circle().perimeter2(6)