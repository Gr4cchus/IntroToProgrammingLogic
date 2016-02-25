# Misleading Percentages
currentInvestmentTotal = 10000
positivePercentageYield = 1.18
negativePercentageYield = .84

firstBiannualDifference = 0.0
secondBiannualDifference = 0.0

for firstMonthSet in range(6):
    currentInvestmentTotal *= negativePercentageYield
    firstBiannualDifference = 10000 - currentInvestmentTotal
    print(format(currentInvestmentTotal, ',.2f'))
    firstInvestmentTotal = currentInvestmentTotal

print()

for secondMonthSet in range(6):
    currentInvestmentTotal *= positivePercentageYield
    secondBiannualDifference = 10000 - currentInvestmentTotal
    print(format(currentInvestmentTotal, ',.2f'))
    secondInvestmentTotal = currentInvestmentTotal - firstInvestmentTotal

print("The first half of the Biannual year saw a loss of", format(firstBiannualDifference, ',.2f'),
      "from initial investment.")
print("The second half of the Biannual year saw a loss of", format(secondBiannualDifference, ',.2f'),
      "from initial investment,\n but a gain of", format(secondInvestmentTotal, ',.2f'),
      "from the previous six months.")
