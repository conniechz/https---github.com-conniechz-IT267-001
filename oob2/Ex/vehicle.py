class Vehicle:
    def __init__(self,name,wheels,max_speed) -> None:
        self.name = name
        self.wheels = wheels
        self._max_speed = max_speed
        self.__vin = None


    def set_vin(self,vin):
        self.__vin = vin

    def v_detail(self):
        print(f'================\nName : {self.name}\n================\nWheels : {self.wheels}\nmaxspeed : {self._max_speed}\nVin : {self.__vin}')