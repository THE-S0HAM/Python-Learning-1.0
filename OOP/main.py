# in python name of the constructor is always __init__()
# In python the first parameter of the constructor is always 'self' which refers to the current instance of the class.

#In python, the first parameter of any method in a class is always 'self' which refers to the current instance of the class.

import math

class Point:
    def __init__(self, a ,b):
        self.x=a
        self.y=b

    def distancefromOrigin(self):
        return math.sqrt((self.x**2)+(self.y**2))

p1=Point(3,4)
print(p1.x,p1.y)
print(p1.distancefromOrigin())

p2=Point(5,7)
print(p2.x,p2.y)
print(p2.distancefromOrigin())