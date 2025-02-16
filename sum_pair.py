# This code takes a list of integers and an integer as input
# Prints the unique pairs of no whose sum is k

# Taking input from the user
numbers = input('Enter comma seperated numbers: ').split(',')
k = int(input('Enter the sum: '))

# Converting the list elements into ints
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

# Declaring a list for storing sets of sum
sum_list = []

# Calculating the sums
for i in range(len(numbers)):
    for j in range(len(numbers) - i):
        if k == numbers[i] + numbers[j]:
            current_set = min(numbers[i], numbers[j]), max(numbers[i], numbers[j])
            sum_list.append(current_set)

# Clearing the duplicate values from the set
sum_list = list(set(sum_list))

# Printing the output
for i in sum_list:
    print(i)