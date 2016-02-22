# Income Tax
myIncome = float(input('Enter taxable income: '))
if myIncome <= 20000:
    tax = .02 * myIncome
    print(tax)
elif myIncome <= 50000:
    tax = 400 + .025 * (myIncome - 20000)
    print(tax)
else:
    tax = 1150 + .035 * (myIncome - 50000)
    print(tax)
