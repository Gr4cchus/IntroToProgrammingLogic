import random


def main():
    while True:
        menu()
        choice = input("Enter your menu selection: ")
        while choice != '1' and choice != '2' and choice != '3' and choice != '4':
            choice = input("Unacceptable selection, pick again : ")
        if choice == '1':
            option1()
        if choice == '2':
            option2()
        if choice == '3':
            option3()
        else:
            break


def read_in(filename):
    try:
        file = open(filename, 'r', encoding='utf-8-sig')
        inData = file.readlines()
        return inData
    except FileNotFoundError:
        print("File is not found.")
        inputFilename = input("Enter the correct filename: ") + '.csv'
        file = open(inputFilename, 'r', encoding='utf-8-sig')
        inData = file.readlines()
        return inData


def data_process(baseballList):
    indexedBodyList = []
    indexedHeaderList = []

    for entry in baseballList:
        entry = entry.replace('"', '').replace(',', ' ').replace('\n', '').replace('Name', "FNAME LNAME").replace(
            "playerid", "playerid AVG").split(' ')
        indexedBodyList.append(entry)
    indexedHeaderList.extend(indexedBodyList.pop(0))
    # print("indexedBodyList:", indexedBodyList)
    # print("indexedHeaderList:", indexedHeaderList)

    avg = 0
    accumulator = 0
    for entry in indexedBodyList:
        # print(entry[4:7:2])
        # print(int(entry[4]), int(entry[6]))
        try:
            avg = int(entry[6]) / int(entry[4])  # H/AB
        except ZeroDivisionError:
            avg = 0
        # print(a)
        indexedBodyList[accumulator].append(str(avg))
        accumulator += 1
    # print(indexedBodyList)
    indexedBodyList.insert(0, indexedHeaderList)
    return indexedBodyList


def write_out(processedBaseballList):
    NyStats = open('NyStats.ah', 'w')
    for entry in processedBaseballList:
        entry = ','.join(entry).replace(',', ' ') + '\n'
        # print(entry)
        NyStats.write(entry)
    NyStats.close()


def menu():
    print("1. Import, clean and covert file")
    print("2. Create a new file from scratch")
    print("3. Search player stats")
    print("4. Quit")


def option1():
    filename = input("Enter the local filename: ") + '.csv'
    inData = read_in(filename)
    processedBaseballList = data_process(inData)
    write_out(processedBaseballList)
    print("The data has been processed")


def option2():  # input_team()
    filename = input("Enter the filename to create: ") + '.csv'
    fw = open(filename, 'a')
    fr = open(filename, 'r')
    header = ["Name", "Age", "G", "AB", "PA", "H", "1B", "2B", "3B", "HR", "R", "RBI",
              "BB", "SO", "HBP", "GDP", "SB", "CS", "SLG", "OPS", "WAR", "Dol", "playerid"]
    isEmpty = fr.readline()
    print(isEmpty)
    if isEmpty == '':
        for entry in header:
            if entry == header[22]:
                fw.write('"' + entry + '"' + '\n')
                break
            fw.write('"' + entry + '"' + ',')

    while True:
    #     for entry in header:
    #         if entry == header[22]:
    #             fw.write('"' + random.randint(20000, 25001) + '"')
    #         fw.write('"' + input("Enter ", entry, ': ', sep='') + '"' + ',')
        fw.write('"' + input("Enter NAME: ") + '"' + ',')
        fw.write('"' + input("Enter Age: ") + '"' + ',')
        fw.write('"' + input("Enter G: ") + '"' + ',')
        fw.write('"' + input("Enter AB: ") + '"' + ',')
        fw.write('"' + input("Enter PA: ") + '"' + ',')
        fw.write('"' + input("Enter H: ") + '"' + ',')
        fw.write('"' + input("Enter 1B: ") + '"' + ',')
        fw.write('"' + input("Enter 2B: ") + '"' + ',')
        fw.write('"' + input("Enter 3B: ") + '"' + ',')
        fw.write('"' + input("Enter HR: ") + '"' + ',')
        fw.write('"' + input("Enter R: ") + '"' + ',')
        fw.write('"' + input("Enter RBI: ") + '"' + ',')
        fw.write('"' + input("Enter BB: ") + '"' + ',')
        fw.write('"' + input("Enter SO: ") + '"' + ',')
        fw.write('"' + input("Enter HBP: ") + '"' + ',')
        fw.write('"' + input("Enter GDP: ") + '"' + ',')
        fw.write('"' + input("Enter SB: ") + '"' + ',')
        fw.write('"' + input("Enter CS: ") + '"' + ',')
        fw.write('"' + input("Enter SLG: ") + '"' + ',')
        fw.write('"' + input("Enter OPS: ") + '"' + ',')
        fw.write('"' + input("Enter WAR: ") + '"' + ',')
        fw.write('"' + input("Enter Dol: ") + '"' + ',')
        fw.write('"' + str(random.randint(20000, 25001)) + '"' + '\n')
        if input("Enter exit, otherwise press enter to continue adding players") == 'exit':
            break
    fw.close()
    fr.close()
    inData = read_in(filename)
    processedBaseballList = data_process(inData)
    write_out(processedBaseballList)    # will write to NyStats.ah though.
    print("The data has been processed")


def option3():
    print("User identified as having to much hair, shave off the excess hair to unlock "
          "this really cool feature.\n")
    # filename = input('Enter the desired filename damnit: ')
    # playerID = input('Enter the desired playerID fat fingers: ')
    # fr = open(filename, 'r', encoding='utf-8-sig')
    # fr.readline()
    # if fr in playerID:
    #     print("")
    # else:
    #     print("not found")

main()
