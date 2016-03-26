# Geometry
from math import sqrt


def main():
    userChoice = menu()
    if userChoice == 'spherical volume':
        r, h = formulaInputs()
        sphereVolume(r)
        menu()
    elif userChoice == 'spherical surface':
        r, h = formulaInputs()
        sphereSurface(r)
        menu()
    elif userChoice == 'cylinder volume':
        r, h = formulaInputs()
        cylinderVolume(r, h)
        menu()
    elif userChoice == 'cylinder surface':
        r, h = formulaInputs()
        cylinderSurface(r, h)
        menu()
    elif userChoice == 'cone volume':
        r, h = formulaInputs()
        coneVolume(r, h)
        menu()
    elif userChoice == 'cone surface':
        r, h = formulaInputs()
        coneSurface(r, h)
        menu()


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
    userDecision = ''
    optionList = ['spherical volume', 'spherical surface', 'cylinder volume',
                  'cylinder surface', 'cone volume', 'cone surface']

    while userDecision not in optionList and userDecision != 'q':  # I really cannot grasp at all
        # why the and was needed and the or wasnt, I thought or just needed one.
        userDecision = input("\n Which of the following calculations "
                             "do you need: spherical volume, spherical surface,\n"
                             "cylinder volume, cylinder surface, cone volume or"
                             "cone surface? Otherwise enter q to quit. ")

        # if unacceptable input, re-prompt user
        if userDecision not in optionList and userDecision != 'q':
            print("\nIncorrect choice, please enter the one of the options precisely.\n")
    return userDecision


def formulaInputs():
    r = float(input("Enter the radius: "))
    h = float(input("Enter the height: "))
    return r, h


main()
