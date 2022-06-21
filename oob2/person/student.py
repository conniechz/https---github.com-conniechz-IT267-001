from person import Person

class Student(Person):
    def __init__(self,name,facully,major,year) -> None:
        super().__init__(name)
        self.facully = facully
        self.major = major
        self.year = year
    
    def welcome(self):
        super().welcome()
        print(f'Welcome to {self.facully} Major {self.major} in {self.year}')