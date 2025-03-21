import random 

def main():
    Number = random.randrange(1,100)
    while True:
        UserNumber = int(input("Guess the number: "))
        if UserNumber == Number:
            print("Congratulations! You guessed the number.")
            break
        elif UserNumber > Number:
            print("Try a smaller number.")
        else:
            print("Try a larger number.")
main()