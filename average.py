# This code takes n integers as input
# Prints the average of these numbers

# Taking input from the user
numbers = input('Enter space seperated numbers: ').split()

# Declaring a variable for sum
sum = 0

# Calculating the sum
for i in numbers:
    sum += int(i)

# Printing the average
print(f'{(sum / len(numbers)):.2f}')