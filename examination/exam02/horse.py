class Horse:
    def __init__(self,max_height:float,name:str,color:str) -> None:
        self.max_height = max_height
        self.name = name
        self.color = color

    def run(self):
        return f'{self.name} is running'

    def show_name(self):
        return f'Horse Name : {self.name}'

    def show_info(self):
        return f'Horse Name : {self.name}\nColor : {self.color}\nMax Height : {self.max_height}'


    