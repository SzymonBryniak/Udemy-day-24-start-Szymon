import os

print(os.getcwd())
#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

input_path = "./input/Letters/starting_letter.txt"
names_path = "./Input/Names/invited_names.txt"

with open(names_path, mode="r") as names:
    name_iter = names.readlines()

for name in name_iter:
    output_path = f"./output/ReadyToSend/example{name.strip()}.txt"
    print(name.strip())
    with open(input_path, mode="r") as letter_template:
        # to_edit = letter.readline()
        to_edit2 = letter_template.read()
        EDITED = to_edit2.replace("[name]", name.strip())

    with open(output_path, mode="w") as letter:
        letter.write(EDITED)

