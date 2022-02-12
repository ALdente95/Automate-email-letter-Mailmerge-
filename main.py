#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
PLACEHOLDER = "[name]"

with open("/Users/andre/PycharmProjects/Mail Merge Project Start/Input/Names/invited_names.txt", "r") as file:
    name_list = file.readlines()

with open(f"/Users/andre/PycharmProjects/Mail Merge Project Start/Input/Letters/starting_letter.txt") as edit_letter:
    edit_letter = edit_letter.read()
    for name in name_list:
        stripped_name = name.strip()
        new_letter = edit_letter.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/{stripped_name}_letter.txt", mode="w") as new_file:
            new_file = new_file.write(new_letter)



