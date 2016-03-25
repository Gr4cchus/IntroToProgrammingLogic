# Paint Job Estimator


def main():
    output()


def num_gallons():
    totalGallons = squareFeet / 112
    if totalGallons % 1 != 0:
        totalGallons += 1
    return int(totalGallons)


def calc_labor_hours():
    laborHours = 8 * num_gallons()
    return laborHours


def calc_paint_cost():
    paintTotal = paintPerPrice * num_gallons()
    return paintTotal


def calc_labor_amt():
    laborCharge = 35 * calc_labor_hours()
    return laborCharge


def total_cost():
    return calc_paint_cost() + calc_labor_amt()


def output():
    print("The number of gallons of paint required is:", num_gallons())
    print("The hours of labor required:", calc_labor_hours())
    print("The cost of the paint is: $", calc_paint_cost(), sep="")
    print("The labor charges are: $", calc_labor_amt(), sep="")
    print("The total cost of the paint job is: $", total_cost(), sep="")


squareFeet = int(input("Enter square feet of wall space to be painted: $"))
paintPerPrice = float(input("Enter the price of paint: $"))

main()
