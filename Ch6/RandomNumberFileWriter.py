# Random Number File Writer
import random
def main():
    file_write()

def file_write():
    fw = open("RandomNumbers.txt", "a")

    runThisManyTimes = int(input("How many random numbers would you like: "))

    for number in range(runThisManyTimes):
        randomNum = random.randint(1, 501)
        print(randomNum)


main()