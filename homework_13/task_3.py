class Auto:
    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0
    def accelerate(self):
        self.speed += 5
    def brake(self):
        self.speed -= 5
        self.speed = max(0, self.speed)
    def display_speed(self):
        print(f'The current speed of {self.brand} {self.model} is {self.speed}')

car = Auto("porshce", "911 turbo s", 2017)
car.brake()
car.display_speed()