def main():
    inData = read_in()
    processedBaseballList = data_process(inData)
    write_out(processedBaseballList)
    print("The data has been processed")


def read_in():
    try:
        file = open('nyyankees.csv', 'r', encoding='utf-8-sig')
        inData = file.readlines()
        return inData
    except FileNotFoundError:
        print("File is not found.")
        inputFilename = input("Enter the correct filename: ")
        file = open(inputFilename, 'r', encoding='utf-8-sig')
        inData = file.readlines()
        return inData



def data_process(baseballList):
    indexedBodyList = []
    indexedHeaderList = []

    for entry in baseballList:
        entry = entry.replace('"', '').replace(',', ' ').replace('\n', '').replace('Name', "FNAME LNAME").replace("playerid", "playerid AVG").split(' ')
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
            avg = int(entry[6]) / int(entry[4])   # H/AB
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

main()
