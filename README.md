# #Coffee-shop-challenge


# # Coffee Shop Domain Model

This project models a Coffee Shop domain using Python's Object-Oriented Programming principles. The project consists of three main classes: Customer, Coffee, and Order. These classes capture the relationships between customers, coffee, and orders.

# Classes and Their Functionalities

# 1. Customer Class (customer.py)

Attributes:

name: The customer's name, must be between 1 and 15 characters.
_orders: A list to store all the orders made by the customer.

Methods:

create_order(coffee, price): Creates an order for a specific coffee and price, associating it with the customer.
orders(): Returns a list of all the orders placed by the customer.
coffees(): Returns a unique list of all the coffee types ordered by the customer.
most_aficionado(coffee): Class method that returns the customer who has spent the most money on the given coffee. If no customer has ordered the coffee, returns None.


# 2. Coffee Class (coffee.py)

Attributes:

name: The name of the coffee, must be at least 3 characters long.

Methods:
orders(): Returns a list of all orders for this coffee.
customers(): Returns a unique list of all customers who have ordered this coffee.
num_orders(): Returns the total number of orders for this coffee.
average_price(): Returns the average price of all orders for this coffee.


# 3. Order Class (order.py)

Attributes:

customer: The customer who placed the order (instance of Customer).
coffee: The coffee associated with the order (instance of Coffee).
price: The price of the coffee, must be a float between 1.0 and 10.0.


This class holds no additional methods but manages the relationships between Customer and Coffee via orders.