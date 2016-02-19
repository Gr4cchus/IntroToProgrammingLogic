# Consumer Price Index
cpi = 238.25
accumulatorYear = 0

while cpi < 476.5:
    cpi *= 1.025
    accumulatorYear += 1
print("Consumer prices will double in", accumulatorYear, 'years.')
