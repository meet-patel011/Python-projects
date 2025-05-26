import random

target = random.randint(1, 100)

while True:
    userChoice = input("Enter a number or Quit: ")
    if(userChoice == "Quit"):
        break
    userChoice = int(userChoice)
    if(userChoice == target):
        print("Success : Correct Guess!")
        break     
    if(userChoice < target):
        print("The number you guess is smaller than target")
    else:
        print("The number you guess is bigger than target")

print("----GAME OVER----")