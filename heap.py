import heapq

arr = [2,1,45,5,6,78]
for i in range(len(arr)):
    arr[i]*=-1
heapq.heapify(arr)
print(arr)

heapq.heappush(arr,19)
heapq.heappush(arr,3)

print(arr)

heapq.heappop(arr)
print(arr)
heapq.heappop(arr)
print(arr)


#methods
# heapify - to create heap from list
# heappop()-delete
# headpush()-insert
# heappushpop()-push item on the heap , then pop and return the smallest
# heapreplace - pop item and return the current smallest value and add the new item
