print('Welcome to Treasure Island.')
print('Your mission is to find the Treasure')
cross_road=input('You\'re at the cross road. Where to go? Type "left" or "right" ')
if(cross_road=='left'):
    print("You have come to the lake. There is an island in the middle of the lake.")
    boat=input('Type "wait" to wait for the boat. Type "swim" to swim across. ')
    if(boat=='wait'):
        print("You have arrived at the island unharmed. There is a house with 3 doors.")
        color=input('One red,one yellow and one blue. Which color do you choose? ')
        if(color=='red'):
            print("its a full room of fire. Game over.")
        elif(color=='yellow'):
            print('You found the treasure! You win!')
        elif(color=='blue'):
            print('You enter room of beast . Game over.')  
    elif(boat=='swim'):
        print('You get attacked by an angry Trout. Game over.')              
elif(cross_road=='right'):
    print("You fell in a hole. Game over.")    