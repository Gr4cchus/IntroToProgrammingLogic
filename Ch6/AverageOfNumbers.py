
def main():
    read_file()


def read_file():
    try:
        fr = open('numbers.txt', 'r')
    except FileNotFoundError:
        print("IOError, issue with file?")

    line = fr.readline()
    accumulator = 0
    numbers = 0
    average = 0
    while line != "":
        try:
            line = int(line)
        except ValueError:
            print("ValueError, issue with number conversion")
            line = fr.readline()
            continue
        accumulator += line
        numbers += 1
        average = accumulator / numbers
        line = fr.readline()
    print('total:', accumulator)
    print('average:', average)
    fr.close()
main()

