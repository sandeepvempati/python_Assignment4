from __future__ import division

class Circle():
    def _init__(self):
        r = self.r
    def area(self,r):
        return 22/7*r*r
    def perimeter(self,r):
        return 2*22/7*r

cir = Circle()
print cir.area(int(raw_input("Enter the radius of circle to find area of circle")))
print cir.perimeter(int(raw_input("Enter the radius of circle to find perimeter of circle")))
