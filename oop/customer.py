class Customer:
    def __init__(self, name: str, loyalty: int):
        self.name = name
        self.loyalty = loyalty

    def __str__(self):
        return "{{name: {}, loyalty: {}}}".format(self.name, self.loyalty)
