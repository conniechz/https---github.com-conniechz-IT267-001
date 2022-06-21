class Bird:
    bird_name = 'Peter'

    def __init__(self,colour) -> None:
        self.colour = colour
        country = 'Thailand'
        print (country)

    def show(self):
        return f'{Bird.bird_name} has {self.colour}'

if __name__ == '__main__':
    my_bird = Bird('Red,Yellow')
    print(my_bird.show())
    