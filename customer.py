class Customer:
    _all_customers = []

    def __init__(self, name):
        self.name = name
        Customer._all_customers.append(self)
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Customer name must be a string between 1 and 15 characters.")

    def orders(self):
        return self._orders

    def coffees(self):
        return list(set(order.coffee for order in self._orders))

    def create_order(self, coffee, price):
        from order import Order
        order = Order(self, coffee, price)
        self._orders.append(order)

    @classmethod
    def most_aficionado(cls, coffee):
        max_spent = 0
        best_customer = None

        for customer in cls._all_customers:
            total_spent = sum(order.price for order in customer.orders() if order.coffee == coffee)

            if total_spent > max_spent:
                max_spent = total_spent
                best_customer = customer

        return best_customer