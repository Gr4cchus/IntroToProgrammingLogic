# Paid in Pennies
days = int(input('How many days? '))
startingMoney = .01
totalMoney = .01

print()
print('Day\t\tSalary\t\tTotal')
print('-------------------------')

for day in range(1, days + 1):
    startingMoney = totalMoney
    totalMoney += totalMoney
    # Tried formatting it with padding but string complications then seem to ensue.
    print(day, str(format(startingMoney, ',.2f')),
          str(format(totalMoney, ',.2f')), sep='\t\t$')
