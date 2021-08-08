"""

This script takes a list of names and inserts them into
a letter to create personalized letters for each person.


"""

import os

PLACEHOLDER = '[name]'
os.chdir('./Output/')
print(os.getcwd())

with open('../Input/Names/invited_names.txt') as names_file:
    names = names_file.readlines()

with open('../Input/Letters/starting_letter.txt') as starting_letter_file:
    starting_string = starting_letter_file.read()


for name in names:
    stripped_name = name.strip()
    new_string = starting_string.replace(PLACEHOLDER, stripped_name)
    with open(f'./ReadyToSend/invited_{stripped_name}.txt', mode='w') as ending_letter_file:
        ending_letter_file.write(new_string)
