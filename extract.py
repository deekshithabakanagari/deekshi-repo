# This code takes a list of strings as input
# Prints the list of no. from the input list

# Taking input from the user
user_input = input('Enter comma seperated elements: ').split(',')

# Declaring a list for storing result
result = []

# Getting the numbers into the result list
for i in user_input:
    if i.isdigit():
        result.append(int(i))

# Printing the output
print(result)