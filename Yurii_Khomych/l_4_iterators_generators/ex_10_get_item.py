class Order:
    def __init__(self, cart, customer):
        self.cart = list(cart)
        self.customer = customer

    def __getitem__(self, key):
        return self.cart[key]


order = Order(["banana", "apple"], "Real Python")
order[0]
order[:-1]


class Inspector:
    def __getitem__(self, key):
        return key


a = Inspector()
a[1]  # => 1: int
a[1, 2]  # => (1, 2): tuple
a[1, 2, 3]  # => (1, 2, 3): tuple
# a[] # => SyntaxError
