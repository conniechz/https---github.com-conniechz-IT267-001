class student:
    def __init__(self,id:str,name:str,major:str = "IT") -> None:
        self.id = id
        self.name = name
        self.major = major
    
    def display_detail(self):
        print(f'ID : {self.id}')
        print(f'Name : {self.name}')
        print(f'Major : {self.major}')

    def __del__(self):
        print('Your information was deleted')

if __name__ == '__main__':
    jessica = student('111','Jessica','IT')
    jessica.display_detail()
    print('******************************')

    john = student('112','John','MKT')
    john.display_detail()
    print('******************************')

    amy = student('113','Amy')
    amy.display_detail()
    print('******************************')