purchase = float(input("Enter the amount of purchase: "))
stateTax = .05 * purchase
countyTax = .025 * purchase
salesTax = stateTax + countyTax
total = stateTax + countyTax + purchase
print("Your subtotal is $" + str(format(purchase, '.2f')))
print("Your state tax is $" + str(format(stateTax, '.2f')))
print("Your county tax is $" + str(format(countyTax, '.2f')))
print("Your total sales tax is $" + str(format(salesTax, '.2f')))
print("Your total is $" + str(format(total, '.2f')))
