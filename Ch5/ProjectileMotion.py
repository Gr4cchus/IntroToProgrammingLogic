# Projectile Motion


def main():
    h, v = get_input()
    maxHeight = max_height(v)


def get_input():
    h = int(input("Enter the initial height: "))
    v = int(input("Enter the initial velocity: "))
    return h, v


# def is_valid(checkValue):


def max_height(v):
    maxHeight = v / 32
    return v


def hit_ground():
    for t in range(25):
        height = h + v * t - 16 * (t ** 2)
        print(height)


main()
