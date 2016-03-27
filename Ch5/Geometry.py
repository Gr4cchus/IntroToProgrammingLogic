# Geometry
from math import sqrt


def main():
    while True:
        menu()

        userChoice = input("Enter your numerical choice or 'q' to exit: ")
        optionList = ['1', '2', '3', '4', '5', '6']

        # while int(userChoice) not in range(1, 7) and userChoice != 'q':
        while userChoice not in optionList and userChoice != 'q':
            userChoice = input("Please enter the precise choice: ")
            # quit program
        if userChoice == 'q':
            break

        # prompt radius
        if int(userChoice) in range(1, 3):
            r = formulaInputs(1)
            if userChoice == '1':
                sphereVolume(r)
            elif userChoice == '2':
                sphereSurface(r)
        # prompt radius + height
        elif int(userChoice) in range(3, 7):
            r, h = formulaInputs(2)
            if userChoice == '3':
                cylinderVolume(r, h)
            elif userChoice == '4':
                cylinderSurface(r, h)
            elif userChoice == '5':
                coneVolume(r, h)
            elif userChoice == '6':
                coneSurface(r, h)


def sphereVolume(r):
    spVolume = (4 / 3) * 3.14159265359 * r ** 3
    print("The volume of the sphere with a radius of",
          r, "is:", format(spVolume, '.5f'))


def sphereSurface(r):
    spSurface = 4 * 3.14159265359 * r ** 2
    print("The surface area of the sphere with a radius of",
          r, "is:", format(spSurface, '.5f'))


def cylinderVolume(r, h):
    cyVolume = 3.14159265359 * r ** 2 * h
    print("The volume of the cylinder with a radius of",
          r, "and height of", h, "is:",
          format(cyVolume, '.5f'))


def cylinderSurface(r, h):
    cySurface = 2 * 3.14159265359 * r * h + \
                2 * 3.14159265359 * r ** 2
    print("The area of the cylinder with a radius of",
          r, "and height of", h, "is:",
          format(cySurface, '.5f'))


def coneVolume(r, h):
    coVolume = 3.14159265359 * r ** 2 * (h / 3)
    print("The volume of the cone with a radius of",
          r, "and height of", h, "is:",
          format(coVolume, '.5f'))


def coneSurface(r, h):
    coSurface = 3.14159265359 * r * (r + sqrt(h ** 2 + r ** 2))
    print("The area of the cone with a radius of",
          r, "and height of", h, "is:",
          format(coSurface, '.5f'))


def menu():
    print("Which calculation is needed?")
    print("1) spherical volume")
    print("2) spherical surface area")
    print("3) cylinder volume")
    print("4) cylinder surface area")
    print("5) cone volume")
    print("6) cone surface area")


def formulaInputs(check):
    if check == 1:
        r = float(input("Enter the radius: "))
        return r
    else:
        r = float(input("Enter the radius: "))
        h = float(input("Enter the height: "))
        return r, h


main()
