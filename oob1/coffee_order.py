class CoffeeOrder:
    menu_type = 'Coffee'
    total = 0
    def __init__(self,customer_name:str,menu:str,num:int=1,size:str='R') -> None:
        self.customer_name = customer_name
        self.menu = menu
        self.num = num
        self.size = size
        self.price = 0
    
    def check_menu(self):
        menu_dictionary = {'- Cafee Mocha (CM)',
                        '- Cappuccino (CP)',
                        '- Americano (AM)',
                        '- Cade Latte (CL)',
                        '- Vanilla Latte (CL)',
                        '- Espresso (ES)'}

    def compute_price(self):
        input('ENTER SIZE : ')
        if self.size == 'L':
            self.size + 1
        if self.size == 'XL':
            self.size + 1.5
            
    
    def display_detail(self):
        print(f'Customer Name = {self.customer_name}')
        print(f'Menu = {self.menu}')
        print(f'Num = {self.num}')
        print(f'Price = {self.price}')
        print(f'Total = {self.total}')

if __name__ == '__main__':
    John = CoffeeOrder('John','Espresso',1)
    John.display_detail()
    print('**********************************')

    Mary = CoffeeOrder('Mary','Americano',2)
    Mary.display_detail()
    print('**********************************')