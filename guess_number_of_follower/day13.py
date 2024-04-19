import followers_data
import logo
import random
import os

def check_more_number(person1,person2):
    choice=input('Who has more followers? Type "A" or "B": ').lower()
    num1=person1['follower_count']
    num2=person2['follower_count']
    if choice=='a':
        return num1>num2
    elif choice=='b':
        return num2>num1

def game():
    count=0
    number1=random.randint(0,49)
    person1=followers_data.data[number1]
    print('Compare A:',person1['name'],", a",person1['description'],', from',person1['country'])
    print(logo.vs)
    number2=random.randint(0,49)
    while number1==number2:
        number2=random.randint(0,49)
    person2=followers_data.data[number2]   
    print('Against B:',person2['name'],", a",person2['description'],', from',person2['country'])
    check=check_more_number(person1,person2)
    os.system('cls')
    while check:
        os.system('cls')
        count+=1
        print('You\'re right! Current score:',count)
        person1=person2
        print('Compare A:',person1['name'],", a",person1['description'],', from',person1['country'])
        print(logo.vs)
        number2=random.randint(0,49)
        person2=followers_data.data[number2]   
        while (person1==person2):
            number2=random.randint(0,49)
            person2=followers_data.data[number2] 
        print('Against B:',person2['name'],", a",person2['description'],', from',person2['country'])
        check=check_more_number(person1,person2)
    os.system('cls')    
    print('Sorry, that\'s wrong. Final score',count)    


def main():
    print(logo.logo)
    game()

if __name__=='__main__':
    main()    
