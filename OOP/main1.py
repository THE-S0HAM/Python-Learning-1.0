import math

class Point:
    def __init__(self, a ,b):
        self.x=a
        self.y=b

    def distancefromOrigin(self):
        return math.sqrt((self.x**2)+(self.y**2))
    
    def midPoint(p1, p2):
        mx= (p1.x+p2.x)/2
        my= (p1.y+p2.y)/2
        p3= Point(mx, my)
        return p3


# p1=Point(3,4)
# print(p1.x,p1.y)
# print(p1.distancefromOrigin())

# p2=Point(5,7)
# print(p2.x,p2.y)
# print(p2.distancefromOrigin())

p1=Point(2,4)
p2=Point(6,8)
p3= Point.midPoint(p1, p2)
print(p3.x, p3.y)
