class Product:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

    def __str__(self):
        return f"name: {self.name}, price: {self.price}"
