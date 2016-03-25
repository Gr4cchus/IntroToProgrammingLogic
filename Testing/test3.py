# Paint Job Estimator

def main():
    squareFeet = int(input("Enter square feet of wall space to be painted: $"))
    paintPerPrice = float(input("Enter the price of paint: $"))

    print("The number of gallons of paint required is:", num_gallons(squareFeet))
    print("The hours of labor required:", calc_labor_hours(squareFeet))
    print("The cost of the paint is: $", calc_paint_cost(paintPerPrice, squareFeet)
          , sep="")
    print("The labor charges are: $", calc_labor_amt(squareFeet), sep="")
    output(paintPerPrice, paintPerPrice)


def num_gallons(squareFeet):
    totalGallons = squareFeet / 112
    if totalGallons % 1 != 0:  # round up
        totalGallons += 1
    return int(totalGallons)


def calc_labor_hours(squareFeet):
    laborHours = 8 * num_gallons(squareFeet)
    return laborHours


def calc_paint_cost(paintPerPrice, squareFeet):
    paintTotal = paintPerPrice * num_gallons(squareFeet)
    return paintTotal


def calc_labor_amt(squareFeet):
    laborCharge = 35 * calc_labor_hours(squareFeet)
    return laborCharge


def total_cost(paintPerPrice, squareFeet):
    return calc_paint_cost(paintPerPrice, squareFeet) + calc_labor_amt(squareFeet)


def output(paintPerPrice, squareFeet):
    print("The total cost of the paint job is: $",
          total_cost(paintPerPrice, squareFeet), sep="")


main()
