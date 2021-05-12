#  I'm emulating Kylie Ying's Madlibs Game

# First I'll create variables using the input function
# which will ask the user for input. 

print('Welcome to Madlibs!')
verb1 = input('Type a verb: ')
verb2 = input('Type a verb: ')
verb3 = input('Type a verb: ')
adjective1 = input('Type a adjective: ')
adjective2 = input('Type a adjective: ')
noun1 = input('Type a noun: ')
noun2 = input('Type a noun: ')
name = input('Type a name: ')
place = input('Name a place: ')

madlib = f"The {adjective1} {noun2} had to {verb1} so urgently, {name} had to {verb2} all the way \
to the {place} where a {adjective2} {noun1} was about to {verb3} for them."

print(madlib)