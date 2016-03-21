print("Inflation\tRules of 72\tActual")
for i in range(1, 21):
    amount = 100
    years = 0
    while amount < 200:
        amount *= 1 + (i/100)
        years += 1
    print(i, "\t\t\t", 72//i, "\t\t\t", years, sep="")
