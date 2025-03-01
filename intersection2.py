# This code takes n sets as input
# Prints the common elements from those n sets

# Taking input for n
n = int(input('How many sets: '))

# Declaring a variable for result
result = set(input('> ').split())

# Taking sets as input
for i in range(n - 1):
    current_set = set(input('> ').split())
    result = result & current_set

# Converting the result to a list
result = list(result)

# Converting the result list elements to ints
for i in range(len(result)):
    result[i] = int(result[i])

# Printing the result
print(sorted(result))