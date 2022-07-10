class Rectangle:
    def __init__(self) -> None:
        self.width = 0
        self.length = 0
        self.area = 0

    def get_data(self):
        self.width = float(input('Enter Width : '))
        self.length = float('Enter Length')

    def compute_area(self):
        self.area = self.width * self.length
    
    def print_area(self):
        print(f'Rectangle Area : {self.area}')

rec_obj = Rectangle()
rec_obj.get_data()
rec_obj.print_area()
3