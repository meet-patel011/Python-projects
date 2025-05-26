import random

computer_choice = random.choice(["rock", "paper", "scissor"])
print("Welcome to rock paper scissor game!")
user_choice = input("Enter your choice: ")
print("Computer's choice was: ", computer_choice)
if computer_choice == "rock" and user_choice == "paper":
    print("you win!")
elif computer_choice == "rock" and user_choice == "scissor":
    print("you loose!")
elif computer_choice == "rock" and user_choice == "rock":
    print("its a draw!")
elif computer_choice == "paper" and user_choice == "rock":
    print("you loose!")
elif computer_choice == "paper" and user_choice == "paper":
    print("its a draw!")    
elif computer_choice == "paper" and user_choice == "scissor":
    print("you win!")
elif computer_choice == "scissor" and user_choice == "rock":
    print("you win!")
elif computer_choice == "scissor" and user_choice == "paper":
    print("you loose!")
elif computer_choice == "scissor" and user_choice == "scissor":
    print("its a draw!")
else:
    print("invalid play!")
