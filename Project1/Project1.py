def main():
    inData = read_in()
    processedBaseballList = data_process(inData)


def read_in():
    file = open('nyyankees.csv', 'r', encoding='utf-8-sig')
    inData = file.readlines()
    return inData


def data_process(baseballList):
    spaceDeliminitedList = []
    headerList = []
    headerIndexedList = []
    indexedBodyList = []

    for entry in baseballList:
        entry = entry.replace('"', '').replace(',', ' ').replace('\n', '')
        spaceDeliminitedList.append(entry)
    print("spaceDeliminitedList:", spaceDeliminitedList)
    headerList.append(spaceDeliminitedList.pop(0))
    print("headerList:", headerList)

    for entry in headerList:
        print(entry)
        entry = entry.replace('Name', "FNAME LNAME").replace("playerid", "playerid AVG").split(' ')
        headerIndexedList.extend(entry)
    print("headerIndexedList:", headerIndexedList)
    print('Fields:', len(headerIndexedList))

    for entry in spaceDeliminitedList:
        entry = entry.split(' ')
        indexedBodyList.extend(entry)
    print("bodyIndexedList:", indexedBodyList)

    # H 6 / AB 4
    return baseballList

# def write_out():

main()
