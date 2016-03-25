#import
from random import randint

#main function
def main():
    compPick = randint(1,3)
    compOut = compchoice(compPick)
    userPick = userinput()
    results(userPick, compPick, compOut)
    again()
#    Uncomment the line below for debug info
#    print(" debug info comppick",comppick, "\n debug info userpick", userpick, "\n debug info compout", compout)


#User input
def userinput():
    userChoice = input("Rock, Paper, or Scissors? ")
    while userChoice != ("Rock") and userChoice != ("Paper") and userChoice != ("Scissors"):
        print(userChoice)
        userChoice = input("That was not a valid choice. Rock, Paper or Scissors? ")

    if userChoice == "Rock":
            userPick = 1
    elif userChoice == "Paper":
            userPick = 2
    elif userChoice == "Scissors":
            userPick = 3

    return userPick

#Converts random number to Rock, Paper or Scissors
def compchoice(compPick):

    if compPick == 1:
        compOut = 'Rock'
    elif compPick ==  2:
        compOut = 'Paper'
    elif compPick == 3:
        compOut = 'Scissors'

    return compOut

#Results
def results(userPick, compPick, compOut):
    if userPick == compPick:
        print("The computer picked", compOut, "Tie")
    elif (userPick == 1 and compPick == 3) or (userPick == 2 and compPick == 1) or (userPick ==3 and compPick == 2):
        print("The computer picked", compOut, "You Win")
    elif (userPick == 1 and compPick == 2) or ( userPick == 2 and compPick == 3) or (userPick == 3 and compPick == 1):
        print("The computer picked", compOut, "You Lose")

def again():
    playAgain = input("Do you want to play again? Yes or No ")
    while playAgain != ("Yes") and playAgain != ("No"):
        print(playAgain)
        playAgain = input("That was not a valid choice. Yes or No? ")

    if playAgain == "Yes":
        main()
    else:
        exit

#Call main
main()


#John Berggren