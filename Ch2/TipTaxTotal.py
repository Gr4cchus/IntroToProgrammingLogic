purchase = float(input("Enter the amount for a meal: "))
salesTax = .07 * purchase
tip = .18 * purchase
total = salesTax + tip + purchase
print("Your sales tax is $" + str(format(salesTax, '.2f')))
print("Your tip is $" + str(format(tip, '.2f')))
print("Your total is $" + str(format(total, '.2f')))
