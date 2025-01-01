def second_largest_element(arr):
    max1 = arr[0]
    max2 = arr[0]
    for i in arr:
        if i>=max1:
            max1