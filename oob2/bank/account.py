class Account:
    def __init__(self) -> None:
        self.type = 'Saving'
        self.number = ''
        self.balance = 0

    def open_account(self,name:str,type,number:str,balance:int = 200):
        self.name = name
        self.type = type
        self.number = number
        self.balance = balance
        
    def display_balance(self):
        return f'{self.name} account = {self.balance} baht'