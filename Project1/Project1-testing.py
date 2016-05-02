def main():
    inData = read_in()
    processedBaseballList = data_process(inData)


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
    for entry in indexedBodyList:
        # print(entry[4:7:2])
        # print(int(entry[4]), int(entry[6]))
        a = int(entry[6]) / int(entry[4])
        print(a)
    # H 6 / AB 4
    return baseballList

# def write_out():

main()
