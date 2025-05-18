from order import Order  

class Coffee:
    all_coffees = []

    def __init__(self, name):
        if isinstance(name, str) and len(name) >= 3:
            self._name = name
            Coffee.all_coffees.append(self)
        else:
            raise ValueError("Coffee name must be at least 3 characters long.")

    @property
    def name(self):
        return self._name
