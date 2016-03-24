# Paint Job Estimator

def main():
    sqft = int(input("Enter square feet of wall space to be painted: "))
    gallons = num_gallons(sqft)
    laborHours = calc_labor_hours(gallons)
    paint = float(input("Enter the price of paint: "))
    paintCost = calc_paint_cost(paint, gallons)
    laborAmount = calc_labor_amt(laborHours)
    totalCost = total_cost(laborAmount, paintCost)
    output(gallons, laborHours, paintCost, laborAmount, totalCost)


def num_gallons(sqft):
    total = sqft / 112
    if total % 1 != 0:
        total += 1
    return int(total)


def calc_labor_hours(gallons):
    return 8 * gallons


def calc_paint_cost(price, gallons):
    return price * gallons


def calc_labor_amt(laborHours):
    return 35 * laborHours


def total_cost(laborAmount, paintCost):
    return laborAmount + paintCost


def output(gallons, laborHours, paintCost, laborAmount, totalCost):
    print("The number of gallons of paint required is:", gallons)
    print("The hours of labor required:", laborHours)
    print("The cost of the paint is: $", paintCost, sep="")
    print("The labor charges are: $", laborAmount, sep="")
    print("The total cost of the paint job is: $", totalCost, sep="")


main()
