def main():
    inData = read_in()
    processedBaseballList = data_process(inData)
    print(processedBaseballList)


def read_in():
    file = open('nyyankees.csv', 'r', encoding='utf-8-sig')
    inData = file.readlines()
    return inData


def data_process(baseballList):
    indexedBodyList = []
    indexedHeaderList = []

    for entry in baseballList:
        entry = entry.replace('"', '').replace(',', ' ').replace('\n', '').replace('Name', "FNAME LNAME").replace("playerid", "playerid AVG").split(' ')
        indexedBodyList.append(entry)
    indexedHeaderList.extend(indexedBodyList.pop(0))
    print("indexedBodyList:", indexedBodyList)
    print("indexedHeaderList:", indexedHeaderList)

    a = 0
    accumulator = 0
    for entry in indexedBodyList:
        # print(entry[4:7:2])
        # print(int(entry[4]), int(entry[6]))
        try:
            a = int(entry[6]) / int(entry[4])
        except ZeroDivisionError:
            a = 0
        print(a)
        indexedBodyList[accumulator].append(str(a))
        accumulator += 1
    print(indexedBodyList)
    # H 6 / AB 4
    final = indexedHeaderList + indexedBodyList
    return final

# def write_out():


main()
