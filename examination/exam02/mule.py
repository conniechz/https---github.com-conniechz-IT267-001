from horse import Horse
from donkey import Donkey

class Mule(Horse,Donkey):
    def __init__(self,max_height:float , name: str, color: str ,age:int, weight:float) -> None:
        Horse.__init__(self, max_height ,name ,color)
        Donkey.__init__(self, age ,weight)

    def run(self):
        return f'Mule is running'   
        
    def show_info(self):
        print(f'**** {self.name} info ****')
        return f'Name : {self.name}\nMax Height : {self.max_height}\nColor : {self.color}\nAge : {self.age}\nWeight : {self.weight}'

mule1 = Mule(200,'Mumu','Blue-eyes cream',3,200)
print(mule1.show_info())
mule2 = Mule(200,'Meme','Palomino',1,120.7)
print(mule2.show_info())
print(mule2.sound())