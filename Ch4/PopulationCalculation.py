# Population Calculation
popChina = 1.37
popIndia = 1.26
accumulatorYear = 2014

while popIndia < popChina:
    popIndia *= 1.0135  # 1.35%
    popChina *= 1.0051  # .51%
    accumulatorYear += 1

print('The country of India will surpass China in population by\n',
      accumulatorYear, 'with', format(popIndia, '.3f'), 'billion people.')
