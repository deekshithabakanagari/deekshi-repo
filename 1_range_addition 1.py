def getModifiedArray(length, updates):
    # Initialize the array with zeros
    result = [0] * length

    # Apply the updates using the difference array concept
    for start, end, increment in updates:
        result[start] += increment
        if end + 1 < length:
            result[end + 1] -= increment

    # Convert the difference array to the final result array
    for i in range(1, length):
        result[i] += result[i - 1]

    return result

# Example usage
length = 5
updates = [
    [1, 3, 2],
    [2, 4, 3],
    [0, 2, -2]
]
print(getModifiedArray(length, updates))  # Output: [-2, 0, 3, 5, 3]
