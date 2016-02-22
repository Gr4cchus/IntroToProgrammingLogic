# Areas of Rectangles, integer
length = int(input('Enter the length: '))
width = int(input('Enter the width: '))

length2 = int(input('Enter the length of the second rectangle: '))
width2 = int(input('Enter the width of the second rectangle: '))

area = length * width
area2 = length2 * width2

if area > area2:
    print("The area of the first rectangle is greater")
elif area == area2:
    print("The areas are equal")
else:
    print('The area of the second rectangle is greater')
