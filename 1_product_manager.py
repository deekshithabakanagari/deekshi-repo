# This code is for effectiveness of meetings questions

def maxMeetings(effectiveness):
    
    # Sort the meetings by their effectiveness impact in descending order
    effectiveness.sort(reverse=True)

    # Initialize variables
    total_index = 0
    count = 0

    # Iterate through the sorted effectiveness list
    for impact in effectiveness:
        if total_index + impact > 0:
            total_index += impact
            count += 1

    return count

# Example usage
effectiveness =  [10, -5, -1, 3, -2, 4, -3, 5, -6, 2]
result = maxMeetings(effectiveness)
print(f"Maximum number of meetings: {result}")  # Output: 3

# Time Complexity: O(n logn)
# Space Complexity: O(1)