from customer import Customer
from coffee import Coffee
from order import Order

cust1 = Customer("Flo")
cust2 = Customer("Silva")

coffee1 = Coffee("Latte")
coffee2 = Coffee("Espresso")
coffee3 = Coffee("Cappuccino")
coffee4 = Coffee("Decaf")

cust1.create_order(coffee1, 5.5)
cust1.create_order(coffee2, 6.0)
cust1.create_order(coffee3, 7.75)


for order in cust1.orders():
    print(f"Order: {order.coffee.name}, Price: ${order.price}")
    print(cust2.name)
    

best_customer = Customer.most_aficionado(coffee1)
if best_customer:
    print(f"The most aficionado for {coffee1.name} is {best_customer.name}.")
else:
    print(f"No customer has ordered {coffee1.name} yet.")