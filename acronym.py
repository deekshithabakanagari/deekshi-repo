# This code takes a string as input
# Prints the acronym of the input

# Taking input from the user
words = input('Enter a sentence: ').split()

# Declaring a variable acronym
acronym = []

# Getting the acronym words
for word in words:
    acronym.append(word[0].upper())

# Joining the alphabets to get the acronym
result = '.'.join(acronym)

# Printing the result
print(result)