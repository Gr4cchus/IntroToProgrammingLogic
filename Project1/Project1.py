def main():
    inData = read_in()
    processedBaseballList = data_process(inData)


def read_in():
    inData = []
    file = open('nyyankees.csv', 'r', encoding='utf-8-sig')

    for line in file:
        inData.append(line)

    file.close()
    return inData


def data_process(baseballList):
    spaceDelimitedList = []
    spaceDelimitedList2 = []
    headerList = []
    headerList2 = []

    print(baseballList)
    for entry in baseballList:
        entry = entry.rstrip('\n').replace(',', ' ').replace('"', '').replace('(', '').replace(')', '')
        spaceDelimitedList.append(entry)
    print("strip,replace:", spaceDelimitedList)

    headerList.append(spaceDelimitedList.pop(0))
    print("header:", headerList)
    for entry in headerList:
        headerList2.append(entry.split(' '))
    print(headerList2)
    # headerList2.insert(0, 'FNAME')
    # headerList2.insert(1, 'LNAME')
    # headerList2.insert(6, 'AVG')
    print(headerList2)

    # for entry in spaceDelimitedList:
    #     spaceDelimitedList2.append(entry.split(' '))
    # print("split:", spaceDelimitedList2)


    return baseballList


#def write_out():


main()

#
#         entry = entry.strip('\n')
#         entry = entry.split(',')
#         entry = ' '.join(entry)
#         entry = entry.split(' ')
