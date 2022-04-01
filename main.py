from customer import Customer
from product import Product
from shoppingcart import ShoppingCart
customer = ('Mike')
banana = Product("Bananas", 3.89, "produce")
orange = Product("Oranges", 1.85, "produce")
pineapple = Product("Pineapple", 2.57, "produce")
dogfood = Product("Purina", 18.99, "petfood")
print(customer.name)

customer.add_item_to_cart(banana)
customer.add_item_to_cart(orange)
customer.add_item_to_cart(pineapple)
customer.add_item_to_cart(dogfood)
customer.cart.calculate_cart_cost()
total_cost = customer.cart.cart_cost
print(total_cost)

customer.cart.empty_cart()

customer.view_cart()
