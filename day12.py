import random
print("Welcome to the number gusiing game!")
print("I'm thinking of a number between 1 and 100")



def guess(attemps,number):
    while attemps!=0:
        guess=int(input("Make a guess: "))
        if  guess<number:
            print("Too low! Try again.")
            attemps-=1
        elif guess>number:
            print("Too high! Try again")
            attemps-=1
        else:
            print("You got it! The answer is",guess) 
            break
        print('You have ',attemps,'attempts remaining to guess the number.')


def easy():
    attempts=10
    num=random.randint(1,100)
    guess(attempts,num)

def hard():
    attempts=5
    num=random.randint(1,100)
    guess(attempts,num)

def main():
    choice=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if choice=='easy':
        easy()
    else:
        hard()


if __name__=='__main__':
    main()    