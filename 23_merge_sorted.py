def merge_sorted(arr1, arr2):
    result = []
    n1 = 0
    n2 = 0
    while n1 < len(arr1) and n2 < len(arr2):
        if arr1[n1] < arr2[n2]:
            result.append(arr1[n1])
            n1 += 1
        else:
            result.append(arr2[n2])
            n2 += 1
    while n1  < len(arr1):
        result.append(arr1[n1])
        n1 += 1
    while n2 < len(arr2):
        result.append(arr2[n2])
        n2 += 1
    return result

print(merge_sorted([1, 2, 3, 4, 5], [2, 4, 6, 8, 10]))

# arr1 = 1 2 3 4 5
#                  ^        
# arr2 = 2 4 6 8 10            
#                  ^
# result = [1, 2, 2, 3, 4 ,4, 5, 6, 8, 10]