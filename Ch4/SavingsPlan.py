# Savings Plan
total = 0.0
accumulatorMonths = 0

while total < 3000:
    total = 1.0025 * total + 100
    accumulatorMonths += 1
print('Annuity will be worth more than $3000 after', accumulatorMonths, 'months.')
