# Paint Job Estimator


def main():
    squareFeet = int(input("Enter square feet of wall space to be painted: "))
    paintPerPrice = float(input("Enter the price of paint: "))

    numberOfGallons = num_gallons(squareFeet)
    laborHours = calc_labor_hours(squareFeet)
    paintCost = calc_paint_cost(paintPerPrice, numberOfGallons)
    laborCost = calc_labor_amt(laborHours)
    totalCost = total_cost(paintCost, laborCost)

    print("The number of gallons of paint required is:", numberOfGallons)
    print("The hours of labor required:", laborHours)
    print("The cost of the paint is: $", format(paintCost, '.2f'), sep="")
    print("The labor charges are: $", format(laborCost, '.2f'), sep="")
    output(totalCost)


def num_gallons(squareFeet):
    total = squareFeet / 112
    if total % 1 != 0:
        total += 1
    return int(total)


def calc_labor_hours(squareFeet):
    hours = squareFeet / 14
    if hours % 1 != 0:
        hours += 1
    return int(hours)


def calc_paint_cost(paintPerPrice, numberOfGallons):
    return paintPerPrice * numberOfGallons


def calc_labor_amt(laborHours):
    return 35 * laborHours


def total_cost(paintCost, laborCost):
    return paintCost + laborCost


def output(totalCost):
    print("The total cost of the paint job is: $", format(totalCost, '.2f'), sep="")


main()
