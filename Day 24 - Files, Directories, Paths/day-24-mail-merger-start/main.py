with open("./Input/Names/invited_names.txt") as names_file:
    names_list = names_file.readlines()

starting_letter = open("./Input/Letters/starting_letter.txt")
starting_contents = starting_letter.read()

for name in names_list:
    formatted_name = name.strip("\n")
    with open(f"./Output/ReadyToSend/letter_for_{formatted_name}.txt", mode="w") as new_letter:
        new_contents = starting_contents.replace("[name]", formatted_name)
        new_letter.write(new_contents)

starting_letter.close()
