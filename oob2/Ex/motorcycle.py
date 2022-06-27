from vehicle import Vehicle

class Motorcycle(Vehicle):
    def __init__(self, name, wheels, max_speed) -> None:
        super().__init__(name, wheels, max_speed)
        self.cc = None

    def set_cc(self,cc):
        self.cc = cc

    def bike_detail(self):
        print(f'cc : {self.cc}')