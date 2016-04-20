def main():
    read_in()


def read_in():
    baseballList = ''
    myList = []
    infile = open('nyyankees.csv', 'r', encoding='utf-8-sig')
    file_contents = infile.readline()

    while file_contents != "":
        # baseballList.append(file_contents)
        # baseballList.append(''.join(file_contents))
        baseballList += file_contents

        print(file_contents)
        file_contents = infile.readline()

    # for entry in baseballList:
    #     print(entry)
    infile.close()
    myList.append(baseballList)
    print(myList)
    return


#def data_process():


#def write_out():


main()