class Donkey:
    def __init__(self,age:int,weight:float) -> None:
        self.age = age
        self.weight = weight

    def sound(self):
        return f'Donkey makes eeoyore sound'
    
    def show_info(self):
        return f'Age : {self.age}-year-old\nWeight : {self.weight}'