from typing import List

from customer import Customer
from product import Product


class ShoppingCart:
    def __init__(self, customer: Customer, products: List[Product]):
        self.customer = customer
        self.products = products

    def __str__(self):
        str_prods = ", ".join("{" + prod.__str__() + "}" for prod in self.products)
        return "{{customer={}, products=[{}]}}".format(self.customer, str_prods)


if __name__ == "__main__":
    customer = Customer("ztx", 100)
    prod1 = Product("byt", 30)
    prod2 = Product("byy", 50)
    cart = ShoppingCart(customer, [prod1, prod2])
    print(cart)
