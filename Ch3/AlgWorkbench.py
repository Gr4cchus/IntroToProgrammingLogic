# Algorithm Workbench
# 1
a = int(input('Enter an integer: '))
if a == 1:
    print('a equals 1')
else:
    print('a is not equal to 1')
# 2
a = int(input('Enter an integer: '))
if a <= 30 and a >= 10: # IDE suggests a different method, 30 >= a >= 10
    a = 20
    print(a)
else:
    print('input not within the range')
# 3
a = int(input('Enter an integer: '))
if a < 10:
    b = 0
    print(b)
else:
    b = 99
    print(b)
#
#
# 5
speed = int(input('Enter your driving speed: '))
if speed > 50:
    print('Speed in limit')
else:
    print('Speed should be checked')
# 6
speed = int(input('Enter your driving speed: '))
if speed >= 24 and speed <= 56:
    print('Speed is normal')
else:
    print('Speed is abnormal')
# 7
points = int(input('Enter point'))
if points < 9 or points > 51:
    print("Invalid points.")
else:
    print('Valid points')
