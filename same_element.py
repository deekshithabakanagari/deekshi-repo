# This code takes a list of integers as input
# Prints true if all the ints are same else prints distinct ints

# Taking input from the user
numbers = input('Enter space seperated numbers: ').split()

# Converting the list elements to ints
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

# Checking if all the no are same
if numbers.count(numbers[0]) == len(numbers):
    print(True)
else:
    print(list(set(numbers)))