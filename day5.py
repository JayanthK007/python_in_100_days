import random

print("welcome to the pypassword generator.")
pass_len=int(input("Enter the length of your password?\n"))
splchar=int(input("How many symbols would you like to ? \n"))
number=int(input("How many numbers would you like? \n"))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



password=[]
for i in range(pass_len):
    password.append(random.choice(letters))

for i in range(number):
     password.append(random.choice(numbers))

for i in range(splchar):
    password.append(random.choice(symbols))

random.shuffle(password)    

string=""
for i in password:
    string+=i

print(string)       

