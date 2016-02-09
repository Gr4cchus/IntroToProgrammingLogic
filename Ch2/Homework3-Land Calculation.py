myFeet = input("Enter the total square feet in a tract of land: ")
acre = int(myFeet) / 43560
if acre > 1:
    print(myFeet + "ft is", str(format(acre, '.4f')) + " acres")
else:
    print(myFeet + "ft is", str(format(acre, '.4f')) + " acre")
