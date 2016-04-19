def main():
    baseballList = read_in()
    processedBaseballList = data_process(baseballList)


def read_in():
    baseballList = []
    file = open('nyyankees.csv', 'r', encoding='utf-8-sig')

    for line in file:
        baseballList.append(line)

    file.close()
    return baseballList


def data_process(baseballList):
    spaceDelimitedList = []
    print(baseballList)

    for entry in baseballList:
        spaceDelimitedList += entry.split("\"")
    print(spaceDelimitedList)
    return baseballList


#def write_out():


main()
