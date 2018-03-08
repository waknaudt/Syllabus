import math
class Circle:
    
    def __init__(self,centro,radio):
        self.centro=centro
        self.radio=radio
    def get_area(self):
        area=math.pi*self.radio**2
        print(area)
c = Circle((0,0),5)
c.get_area()
