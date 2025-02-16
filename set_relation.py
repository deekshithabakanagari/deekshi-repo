# This code has a set and takes another set as input
# Prints the relation between the sets

# Defining the set
num_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}

# Taking input from the user
numbers = input('Enter space seperated numbers: ').split()

# Converting the list elements to ints
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

# Converting the input list into a set
numbers = set(numbers)

# Checking the relation
if num_set.issubset(numbers):
    print('Subset')
elif num_set.issuperset(numbers):
    print('Superset')
elif num_set.isdisjoint(numbers):
    print('Disjoint')