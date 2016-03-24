# Misleading Percentages
investment = 10000
gain = 1.18
loss = .84
total = 0

for biannual in range(2):
    for months in range(6):
        if biannual == 0:
            investment *= loss
        else:
            investment *= gain
print('The value of the stock at the end of the year is: $',
      format(investment, '.2f'), sep="")
