# Quadratic Equation
from math import sqrt  # or import math

a = float(input('What is a?: '))
b = float(input('What is b?: '))
c = float(input('What is c?: '))

discriminant = b**2 - 4 * a * c

if discriminant > 0:
    r1 = (-b + sqrt(discriminant)) / (2 * a)
    r2 = (-b - sqrt(discriminant)) / (2 * a)
    print('Root one is: ', format(r1, '.2f'),
          '\nRoot two is: ', format(r2, '.2f'), sep='')
elif discriminant == 0:
    r1 = (-b + sqrt(discriminant)) / (2 * a)  # sqrt must turns this to float?
    print('The discriminant is 0 so the root is: ', end='')
    print(format(r1, '.2f'))
else:
    print('The equation has no real roots')
