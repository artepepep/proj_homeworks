class Restaurant:
    def __init__(self, name, cuisine, menu: dict):
        self.name = name
        self.cuisine = cuisine
        self.menu = menu
class FastFood(Restaurant):
    # your code here
    pass

menu =  {
    'burger': {'price': 5, 'quantity': 10},
    'pizza': {'price': 10, 'quantity': 20},
    'drink': {'price': 1, 'quantity': 15}
}

mc = FastFood('McDonalds', 'Fast Food', menu, True)

print(mc.order('burger', 5)) # 25
print(mc.order('burger', 15)) # Requested quantity not available
print(mc.order('soup', 5)) # Dish not available