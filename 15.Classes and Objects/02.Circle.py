class Circle:
    _pi=3.14
    def __init__(self,diameter:int):
        self.diameter=diameter
        self.radious=diameter/2

    def calculate_circumference(self):
        return self._pi*2*self.radious
    def calculate_area(self):
        return self._pi*self.radious**2
    def calculate_area_of_sector(self,angle):
        self.angle=angle
        return self.angle/360*self._pi*self.radious**2
