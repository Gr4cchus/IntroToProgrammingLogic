# Projectile Motion


def main():
    h, v = get_input()
    max_height(v)
    hit_ground(h, v)


def get_input():
    h = float(input("Enter the initial height: "))
    v = float(input("Enter the initial velocity: "))
    while is_valid(h) is False or is_valid(v) is False:
        if is_valid(h) is False:
            h = float(input("That height is unacceptable, enter the initial height again: "))
        if is_valid(v) is False:
            v = float(input("That velocity is unacceptable, enter the initial velocity again: "))
    return h, v


def is_valid(checkValue):
    if checkValue > 0:
        return True
    else:
        return False


def max_height(v):
    maxHeight = v / 32
    print("The maximum height of the ball will be", format(maxHeight, '.2f'), "feet.")


def hit_ground(h, v):
    t = 0
    height = 1
    while height >= 0:
        t += .1
        # for t in range(25):
        height = h + v * t - 16 * (t ** 2)
    print("The ball will hit the ground after", format(t, '.2f'), "seconds.")


main()
