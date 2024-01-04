import os
from leadergpu import LeaderGPUClient

CLIENT_ID = os.environ['LEADERGPU_CLIENT_ID']
CLIENT_SECRET = os.environ['LEADERGPU_AUTH_TOKEN']

leadergpu = LeaderGPUClient(CLIENT_ID, CLIENT_SECRET)

# Get all products
products = leadergpu.products.get()

# Filter out products that are available
free_products = [product for product in products if product.free_time == None]
# Sort products by price and get the product with the lowest price
free_product = sorted(free_products, key=lambda product: product.price)

# Print the available sorted by the lowest price
for product in free_product:
    print(product)

# Order a the selected server, change the parameters accordingly example:
# product_id = 909
# os = 'ubuntu'
# period_count = 300
# Note the total cost has to be > 10 Euros, for a successful transaction
product_id = 909
os = 'ubuntu'
period_count = 200
leadergpu.servers.order(product_id, os, period_count)
