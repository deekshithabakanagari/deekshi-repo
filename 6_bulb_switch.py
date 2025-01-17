def bulb_switch(arr):
    result = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            for j in range(i, len(arr)):
                arr[j] = 0 if arr[j] == 1 else 1
            result += 1
    return result
    
print(bulb_switch([0, 1, 0, 1]))

# Not Solved