# Supply and Demand
soybeanQuantity = 80.00
startingPrice = 12.00

print("YEAR", "QUANTITY", "PRICE", sep="\t\t")
print("2014", soybeanQuantity, startingPrice, sep="\t\t")

for year in range(2015, 2019):
    startingPrice = 20 - .1 * soybeanQuantity
    soybeanQuantity = 5 * startingPrice - 10
    print(year, soybeanQuantity, startingPrice, sep="\t\t")
