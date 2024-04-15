import os

logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''


print("Welcome to the secret aution program.")
print(logo)
choice='yes'
biddings={}
while choice=='yes':
    name=input('What\'s your name?: ')
    bid=int(input('what\'s your bid?: $'))
    biddings[name]=bid
    choice=input('Are there  any other bidders? Type "Yes" or "No".').lower()
    if(choice=='yes'):
        os.system(r'cls')

os.system(r'cls')
max=0
for key,val in biddings.items():
    if(max<val):
        max=val    

winner=""
for val in biddings.keys():
    if max==biddings[val]:
        winner=val  

print(f'The winner is {winner} with a bid of ${max}')             
