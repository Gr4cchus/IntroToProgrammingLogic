import random

def(main):
    students = ['name', 'name2', 'name3', 'name4']
    fw = open("MWTeam", 'w')    # will create a file named MWTeam and 'w' will allow write access (r,w,a are options)

    team = []
    upper = 14
    for i in range(5):
        for k in range(3):
            random.randint(0,upper)     # why specify upper?
            append.team(students.pop(z))    # append puts in, pop takes out
            upper -= 1
        fw.write(team[0]+ '' + team[])