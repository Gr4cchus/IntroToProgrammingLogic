def main():
    while True:
        try:
            x = int(input("Enter the first integer: "))
            y = int(input("Enter the first integer: "))
            print(x/y)

            break # will enter out of the loop after valid numbers are entered
        except ValueError:
            print("Value not acceptable")
        # print(x/y)  # move this into the try block so when dividing by zero it will get caught
        except ZeroDivisionError:
            print("You cannot divide by zero!")
            # Be specific in your errors

main()
