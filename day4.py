import random

choice = input("what do you choose? Type 0 for Rock,Type 1 for Paper,Type 2 for Scissor ")
game=['Rock','Paper','Scissor']

if(int(choice)<0 or int(choice)>2):
    print('Enter valid input in the range 0-2')

print('user choice: ',game[int(choice)])

comp_choice=random.randint(0,2)
print('computer choice: ',game[comp_choice])


if(int(choice)==comp_choice):
    print("It a tie play again")
elif(choice=='0' and comp_choice==1):
    print('You chose rock and computer chose paper , Computer win you lose')
elif(choice=='1' and comp_choice==2):
    print('You chose paper and computer chose scissor , Computer win you lose')     
elif(choice=='2' and comp_choice==0):
    print('You chose scissor and computer chose rock , Computer win you lose')
elif(choice=='0' and comp_choice==2):
    print('you chose rock and computer chose scissor, you win')      
elif(choice=='1' and comp_choice==0):
    print('you chose paper and computer chose rock, you win') 
elif(choice=='2' and comp_choice==1):
    print('you chose scissor and computer chose paper, you win')  