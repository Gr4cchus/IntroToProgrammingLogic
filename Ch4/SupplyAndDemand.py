# Supply and Demand
quantity = 80
price = 18

print("Year", "Quantity", "Price", sep="\t\t")

for year in range(2014,2019):
    quantity = 5 * price - 10
    price = 20 - .1 * quantity
    print(year, quantity, price, sep="\t\t")
