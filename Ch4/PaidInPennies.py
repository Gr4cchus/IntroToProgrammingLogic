# Paid in Pennies
days = int(input('How many days? '))
startingMoney = .01
totalMoney = .01

print()
print('Day\t\tSalary\t\tTotal')
print('-------------------------')

for x in range(1, days + 1):
    startingMoney = totalMoney
    totalMoney += totalMoney
    totalMoneyFormat = format(totalMoney, ',.2f')
    startingMoneyFormat = format(startingMoney, ',.2f')
    print(x, '\t\t$' + str(startingMoneyFormat), '\t\t$' + str(totalMoneyFormat))
