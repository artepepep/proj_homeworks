class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity
class Book(Product):
    def __init__(self, name, price, quantity, author: str):
        super().__init__(name, price, quantity)
        self.author = author
    def read(self):
        print(f'name: {self.name}\nauthor: {self.author}\nprice: ${self.price}\nquantity: {self.quantity}')
book_number_1 = Book("Loards of the rings", 15.50, 97, "John Ronald Reuel Tolkien")
book_number_1.read()