#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Letters/starting_letter.txt") as file:
    contents=file.readlines()
with open("Input/Names/invited_names.txt") as file:
    names=file.read().split()

for name in names:
    with open(f"Output/ReadyToSend/lettet_to_{name}.txt",'w') as file:
        for index in range(len(contents)):
            if index==0:
                new_line=f'Dear {name},\n'
                contents[0]=new_line
            file.write(contents[index])
