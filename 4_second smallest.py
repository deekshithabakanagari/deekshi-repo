def secondsmallest(arr):
    smallest = second_smallest = float("inf")
    for i in range(len(arr)):
        if arr[i]<smallest:
            second_smallest = smallest
            smallest = arr[i]
        elif arr[i]<second_smallest and arr[i]!=smallest:
            second_smallest = arr[i]

    return second_smallest
arr = [12,13,4,34,56,78,78,90,90,7]
print(secondsmallest(arr))
#O(N)
#O(1)