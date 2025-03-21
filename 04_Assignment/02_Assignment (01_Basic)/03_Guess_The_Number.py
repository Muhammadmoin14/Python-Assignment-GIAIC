import random

def play_guess_number():
    random_number = random.randrange(0, 99)
    print('Welcome to Guess My Number!')
    print('I am thinking of a number between 0 and 99')
    
    while True:
        try:
            user_input = int(input('Enter your guess (0-99): '))
            if user_input < 0 or user_input > 99:
                print('Please enter a number between 0 and 99')
                continue
                
            if user_input < random_number:
                print('Too Low')
            elif user_input > random_number:
                print('Too High')
            else:
                print(f'You Won! The number was {random_number}')
                play_again = input('Would you like to play again? (y/n): ')
                if play_again.lower() != 'y':
                    break
                random_number = random.randrange(0, 99)
                print('\nNew game started!')
                print('I am thinking of a number between 0 and 99')
                
        except ValueError:
            print('Please enter a valid number')

if __name__ == "__main__":
    play_guess_number()







# import random
# import streamlit as st

# st.title('Guess My Number')
# st.write('I am thinking of a number between 0 and 99')
# UserInput = st.number_input('Enter the Guess ',max_value=99,min_value=0,step=1)

# if 'RandomNumber' not in st.session_state:
#     st.session_state.RandomNumber = random.randrange(0,99)


# st.write(st.session_state.RandomNumber)

# def NumberCheck():   
#     if UserInput < st.session_state.RandomNumber:
#         return 'Too Low'
#     elif UserInput > st.session_state.RandomNumber:
#         return 'Too High'
#     else:
#         return f'You Won {st.session_state.RandomNumber}'
#         st.session_state.RandomNumber = random.randint(0, 99)
# Result = NumberCheck()
# st.write(Result)

