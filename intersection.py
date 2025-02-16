# This code takes three sets as input
# Prints the common elements of the three sets

# Taking input from the user
set_1 = input('Enter comma seperated numbers: ').split()
set_2 = input('Enter comma seperated numbers: ').split()
set_3 = input('Enter comma seperated numbers: ').split()

# Checking for the common elements
temp = set(set_1) & set(set_2)
result = list(set(set_3) & temp)

# Converting the result elements to ints
for i in range(len(result)):
    result[i] = int(result[i])

# Printing the output
print(result)