time = input('Enter the military time: ')
time1 = int(time[0:2]) # if you leave the start index (0) out, default assumes 0
time2 = time[2:4]

# am or pm
if time1 >= 12:
    period = 'pm'
else:
    period = 'am'
# if 00xx turn to 12
if time1 == 0:
    time1 = 12
# Format hours
if time1 >= 13:
    time1 = time1 - 12 # IDE "Assignment can be replaced with augmented assignment", idk what its referring to

print('The time is', end=' ')
print(time1, time2, sep=':', end='')
print(period, 'in standard time.')