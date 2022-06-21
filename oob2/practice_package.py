from cusorder.customer import Customer
from cusorder.order import Order

cus1 = Customer('Jame','Nonthaburi')
cus_order = Order('15-06-2022','Packed')

print(f'Order of {cus1.name} on {cus_order.date} is {cus_order.status}')