purchaseOne = float(input("Enter 1st item: "))
purchaseTwo = float(input("Enter 2nd item: "))
purchaseThree = float(input("Enter 3rd item: "))
purchaseFour = float(input("Enter 4th item: "))
purchaseFive = float(input("Enter 5th item: "))
subtotal = purchaseOne + purchaseTwo + purchaseThree + purchaseFour + purchaseFive
salesTax = .07 * subtotal
total = subtotal + salesTax
# should format( ,.2f) in future.
print("Your subtotal is $" + str(format(subtotal, '.2f')))
print("Your sales tax is $" + str(format(salesTax, '.2f')))
print("Your total is $" + str(format(total, '.2f')))
