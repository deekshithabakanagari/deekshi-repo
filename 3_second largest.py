# def second_largest(arr):
#     largest = float('-inf')
#     second_largest = float('-inf')
#     for  i in range(len(arr)):
#         if arr[i]>largest:
#             second_largest = largest
#             largest = arr[i]
#         elif arr[i]>second_largest and arr[i]!=largest:
#             second_largest = arr[i]

#     return second_largest if second_largest != float('-inf') else -1

# arr = [10, 10, 10]
# print(second_largest(arr))

# #O(N)
# #O(1)

# def longest_repeating_substring(s):
#     n = len(s)
#     longest = 0
    
#     # Start from longest possible substring and reduce length
#     for i in range(n, 0, -1):
#         seen = set()
        
#         # Generate all substrings of 'i'
#         for j in range(n - i + 1):
#             sub = s[j:j+i]
#             if sub in seen:
#                 return i  # Found longest repeating substring
#             seen.add(sub)
    
#     return 0  # No repeating substring found

# # Example test cases
# s1 = "aaaa"
# s2 = "aabcaabdaab"

# print(longest_repeating_substring(s1))  # Output: 3
# print(longest_repeating_substring(s2))  # Output: 3


# def longestDupSubstring(s):
#         n = len(s)
#         longest_substring = ""

#         # Try all possible substring lengths
#         for length in range(n, 0, -1):
#             seen = set()
            
#             # Generate all substrings of 'length'
#             for i in range(n - length + 1):
#                 sub = s[i:i+length]
#                 if sub in seen:
#                     return sub  # Found longest duplicated substring
#                 seen.add(sub)
        
#         return "" 


# s = "abcd"
# print(longestDupSubstring(s))

def sumPrefixScores(words):
    result = []
    
    # Iterate through each word
    for word in words:
        total_score = 0
        
        # Count occurrences of each prefix in the entire list
        for i in range(1, len(word) + 1):
            prefix = word[:i]
            total_score += sum(w.startswith(prefix) for w in words)
        
        result.append(total_score)

    return result

# Example test cases
print(sumPrefixScores(["abc","ab","bc","b"]))  # Output: [5,4,3,2]
print(sumPrefixScores(["abcd"]))  # Output: [4]
