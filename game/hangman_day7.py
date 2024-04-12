import random
from word_list import word_list
from logo import stages,logo


print(logo)

lives=6

words=random.choice(word_list)

ans=[]
for _ in range(len(words)):
    ans.append('_')
 

while ans!=list(words) and lives!=0:
    user_word=input(f"guess the letter in the word :").lower()

    if user_word in ans:
        print(f'\nYou have already guessed the letter {user_word}. Please try a different letter\n')

    if user_word not in words:
        print(f'\nYou guessed a letter {user_word} and that is not in the word. You lose a life.\n')
        lives-=1
        print()


    for i in range(len(words)):
        if(user_word in words[i]):
            ans[i]=user_word
    print(stages[lives])    
        

    print(ans) 

if ans==list(words):
    print("\nYou won")   
else:
    print('\nYou lost')    




