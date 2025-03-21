import random

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    n=0
    while N_NUMBERS > n:
        number = random.randint(MIN_VALUE, MAX_VALUE)
        print(number)
        n+=1

if __name__ == '__main__':
    main()
