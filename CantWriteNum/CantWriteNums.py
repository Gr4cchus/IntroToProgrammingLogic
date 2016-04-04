def main():
    fw = open('nums.txt', 'w')

    for i in range(1,6):
        fw.write(str(i) + '\n')  # Cannot write i to file because a int + string, convert when writing numbers

    fw.close()


main()