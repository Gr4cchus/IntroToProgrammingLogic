def main():
    read_in()


def read_in():
    baseballList = []
    infile = open('nyyankees.csv', 'r')
    file_contents = infile.readline()

    while file_contents != "":
        baseballList.append(file_contents)
        print(file_contents)
        file_contents = infile.readline()

    infile.close()
    print(baseballList)
    return


#def data_process():


#def write_out():


main()