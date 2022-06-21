class car:
    def __init__(self,model,colour,year,price) -> None:
        self.model = model
        self.colour = colour
        self.year = year
        self.price = price
    
    #instace method ต้องมี self
    def price_detail(self):
        print(f"Model : {self.model}")
        print(f"Colour : {self.colour}")
        print(f"Year : {self.year}")
        print(f"Price : {self.price}")
        
    def abc(self):
        print(f"Year : {self.year}")
    #static method ไม่ต้อง self
    def get_static_method(text) #มี 1 argument คือ text
        print(f"String : {text}")

    def get_class_method(cls,text):
        print(f"This is class method with {text}")

if __name__ == "_main_":
    my_car = car("Cross","White",2022,1500000)
    #call instance method
    my_car.price_detail()
    #Call static method
    car.get_static_method("Hello")
    my_car.get_static_method("Good Car")
    car.get_class_method("Go Home")