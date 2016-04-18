def main():
    read_in()


def read_in():
    baseballList = []
    file = open('nyyankees.csv', 'r', encoding='utf-8-sig')

    for line in file:
        baseballList.append(line)

    file.close()
    print(baseballList)
    return


#def data_process():


#def write_out():


main()