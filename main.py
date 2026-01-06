import random

computer= random.choice([-1,0,1])
youDict={"s" : 1 ,"w" : -1,"g":0 }
reverseDict={1: "Snake",-1: "Water", 0:"Gun"}

youstr = input("Enter your choice (s, w, g): ").lower()

if youstr not in youDict:
    print("Invalid input! Please choose s, w, or g.")
    exit()

you=youDict[youstr]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("Its a draw")
else:
    if(computer == -1 and you == 1):
        print("You Win!")
    elif(computer == -1 and you == 0):
        print("You Lose!")
    elif(computer == 1 and you == -1):
        print("you Lose!")
    elif(computer == 1 and you == 0):
        print("You Win!")
    elif(computer == 0 and you == -1):
        print("You Win!")
    elif(computer == 0 and you == 1):
        print("You Lose!")
    else:
        print("Something wen wrong")