# Cramers Rule
a = float(input('What is a?: '))
b = float(input('What is b?: '))
c = float(input('What is c?: '))
d = float(input('What is d?: '))

e = float(input('What is e?: '))
f = float(input('What is f?: '))

xTopLine = e * d - b * f
yTopLine = a * f - e * c
divisor = a * d - b * c

if divisor == 0:
    print("The equation has no solution")
else:
    x = xTopLine / divisor
    y = yTopLine / divisor
    print('x is: ', x,
          '\ny is: ', y)
