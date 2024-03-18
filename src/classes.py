class Category:
    name: str
    description: str
    product: str
    number_of_categories = 0
    unique_product = 0

    def __init__(self, name, description, product):
        self.name = name
        self.description = description
        self.product = product

        Category.number_of_categories += 1
        Category.unique_product += 1


class Product:
    name: str
    description: str
    price: float
    availability: int

    def __init__(self, name, description, price, availability):
        self.name = name
        self.description = description
        self.price = price
        self.availability = availability
