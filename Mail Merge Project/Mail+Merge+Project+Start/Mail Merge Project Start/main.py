# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as file_names:
    names = file_names.readlines()
    # The readlines() method returns a list containing each line in the file as a list item.
    print(names)

with open("./Input/Letters/starting_letter.txt") as file_letter:
    letter_content = file_letter.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
        print(new_letter)
        with open(f"./Output/ReadyToSend/letter for {stripped_name}.txt", mode='w') as completed_letter:
            completed_letter.write(new_letter)
