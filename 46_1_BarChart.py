# Create a bar chart using matplotlib to visualize sales data.

import matplotlib.pyplot as plt

# Get number of products
num = int(input("Enter number of products: "))

products = []
sales = []

# Take user input
for i in range(num):
    product = input(f"Enter name of product {i+1}: ")
    sale = float(input(f"Enter sales for {product}: "))
    products.append(product)
    sales.append(sale)

# Create the bar chart
plt.figure(figsize=(10, 6))
plt.bar(products, sales, color='lightgreen')

# Add titles and labels
plt.title('Sales Data from User Input')
plt.xlabel('Products')
plt.ylabel('Units Sold')

# Show the chart
plt.tight_layout()
plt.show()
