import random

def rock_paper_scissor():
    while True:
        computer_choice = random.choice(['rock', 'paper', 'scissor'])
        user_choice = input("Enter your choice: ").lower()
        print(computer_choice,user_choice)
        if computer_choice == user_choice:
            print("It's a tie!")
        elif (computer_choice == 'rock' and user_choice == 'scissor')or (computer_choice == 'scissor' and user_choice == 'paper') or (computer_choice == 'paper' and user_choice == 'rock'):
            print("Computer wins!")
        else:
            print("You win!")
            break

rock_paper_scissor()