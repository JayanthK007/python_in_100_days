import random

choice=input("Do you want to play the blackjack? Type 'y' or 'n': ")
continue_game=True
new_game=True
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
if choice=='y':
    pass
else:
    continue_game=False

def random_cards():
    return random.choice(cards)    


while continue_game:
    if new_game:
        my_cards=[random_cards(),random_cards()]
        computer_card=[random_cards(),random_cards()]
        print('your cards:',my_cards,'current score:',sum(my_cards))
        print('Computer\'s first card:',computer_card[0])  
    pick=input("Type 'y' to get another card, type 'n' to pass: ")
    if pick=='y':
        new_game=False
        my_cards.append(random.choice(cards))
        computer_card.append(random.choice(cards))
        if my_cards[-1]==11:
            if sum(my_cards)>21:
                my_cards[-1]=1
        print('your cards:',my_cards,'current score:',sum(my_cards))
        print('Computer\'s first card:',computer_card[0])
            
        if(sum(my_cards)>21):
            print("You have busted!, Computer wins!")
            continue_game=False
        if sum(computer_card[0:-1])==21:
            print('Computer\'s final hand:',computer_card,'current score:',sum(computer_card[0:-1]))
            print('Computer wins')
            continue_game=False
        elif sum(my_cards)==sum(computer_card[0:-1]) and sum(my_cards)<21 and  sum(computer_card[0:-1])<21:
            print('Computer\'s final hand:',computer_card,'current score:',sum(computer_card[0:-1]))
            print("Draw")
            continue_game=False 
        elif  sum(computer_card[0:-1])<21:
            computer_card[-1]=random.choice(cards)    
    else:
        print('Your final hand:',my_cards,'current score:',sum(my_cards))
        print('Computer\'s final hand:',computer_card,'current score:',sum(computer_card))
        player_sum=sum(my_cards)
        computer_sum=sum(computer_card)
        if(player_sum==21):
            print('You win')   
        elif (computer_sum==21):
            print('Computer wins.')   
        elif(computer_sum>21):
            print('You win.')
        elif( player_sum<21  and player_sum>computer_sum):
                print('You win')   
        elif( computer_sum<21 and player_sum<computer_sum ):
            print('Computer wins.')
        else:
            print("Draw")    

        choice=input("Do you want to play the blackjack game again? Type 'y' or 'n': ")  
        if choice=='n':
            continue_game=False 
        else:
            new_game=True         
              


print("Thank you!")        