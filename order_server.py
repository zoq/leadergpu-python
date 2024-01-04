import os
from leadergpu.leadergpu import LeaderGPUClient

CLIENT_ID = os.environ['LEADERGPU_CLIENT_ID']  # Replace with your client ID
CLIENT_SECRET = os.environ['LEADERGPU_AUTH_TOKEN']

# Create LeaderGPU client
leadergpu = LeaderGPUClient(CLIENT_ID, CLIENT_SECRET)

products = leadergpu.products.get()

# Filter out products that are available
free_products = [product for product in products if product.free_time == None]
# Sort products by price and get the product with the lowest price
free_product = sorted(free_products, key=lambda product: product.price)

# # Create a new instance
# print(free_product)

# for product in free_product:
#     print(product)
#     print("---------------")

print(leadergpu.servers.order(909, 'ubuntu', 200))
# 909


# print(foo)

# for product in free_products:
#     print(product)
#     print("---------------")

# # Create a new instance
# leadergpu.instances.create()