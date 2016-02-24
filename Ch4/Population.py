# 12 Population
startingPopulation = float(input("Enter organism starting number: "))
dailyAverageMultiplier = float(input("Enter daily percentage growth as a integer: ")) / 100 + 1
dailyCycles = int(input("Enter number of days left to multiply: "))

print("\nDay Approximate\t\t\tPopulation")
print(1, startingPopulation, sep="\t\t\t\t\t\t")

for days in range(2, dailyCycles + 1):
    startingPopulation *= dailyAverageMultiplier
    print(days, format(startingPopulation, '.5f'), sep="\t\t\t\t\t\t")
