# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(key,value)

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     print(index,row)
#     #Access row.student or row.score
#     print(row.student,row.score)
import pandas
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
phonetic_alphabet=pandas.read_csv('nato_phonetic_alphabet.csv')
new_dictionary={row.letter:row.code for(index,row) in phonetic_alphabet.iterrows()}


   


#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
while True:
    try:
        user_input=input("Enter a word: ")
        new_word=[new_dictionary[word] for word in user_input.upper()]
    except KeyError: 
        print("Sorry, only letters in the alphabets are allowed.")
    else:       
        print(new_word)
        break

