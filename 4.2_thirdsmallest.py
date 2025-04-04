def thirdsmallest(arr):
    smallest = second_smallest = third_smallest = float("inf")
    for i in range(len(arr)):
        if arr[i]<smallest:
            third_smallest = second_smallest
            second_smallest = smallest
            smallest = arr[i]
        elif arr[i]<second_smallest and arr[i]!=smallest:
            third_smallest = second_smallest
            second_smallest = arr[i]

        elif arr[i]<third_smallest and arr[i]!=second_smallest and arr[i]!=smallest:
            third_smallest=arr[i]
    return third_smallest
arr = [12,13,4,34,56,78,78,90,90,7]
print(thirdsmallest(arr))