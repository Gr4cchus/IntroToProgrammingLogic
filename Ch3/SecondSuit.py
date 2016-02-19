# Second Suit
firstSuit = float(input('Enter the price of the first suit: '))
secondSuit = float(input('Enter the price of the second suit: '))
total = 0
if firstSuit >= secondSuit:
    discountSuit = secondSuit * .5
    total = firstSuit + discountSuit
elif secondSuit >= firstSuit:   # is it better practice to use else instead, /
    # or is else used for something more fundamentally different?
    discountSuit = firstSuit * .5
    total = secondSuit + discountSuit
print('The total is $', format(total, '.2f'), sep='')   # IDE complained of total undefined variable /
# despite it working, is it better to define the variables I used in my control structure before /
# creating them inside the structure, I could maybe see that becoming a problem in the future?
