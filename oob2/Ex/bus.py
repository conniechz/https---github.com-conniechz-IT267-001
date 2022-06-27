from vehicle import Vehicle

class Bus(Vehicle):
    def __init__(self, name, wheels, max_speed) -> None:
        super().__init__(name, wheels, max_speed)
        self.color = None
        self.capacity = None

    def set_color(self,color):
        self.color = color

    def set_capacity(self,capacity):
        self.capacity = capacity

    def bus_detail(self):
        print(f'Color : {self.color}\nCapacity : {self.capacity}')