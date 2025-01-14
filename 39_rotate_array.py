def rotate_array(arr, k):
    for i in range(k):
        temp = arr.pop(-1)
        arr.insert(0, temp)
    return arr

print(rotate_array([1, 2, 3, 4, 5, 6, 7], 3))