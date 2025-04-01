# # Brute force
# # rotate array by d places

# def arrayrotate(arr):
#     temp =arr[0]
#     temp1 = arr[1]
#     temp2 = arr[2]
#     for i in range(3,len(arr)):
#         arr[i-3] = arr[i]
#     arr[-1] = temp
#     arr[-2] = temp1
#     arr[-3] = temp2
#     return arr
# arr = [1,2,3,4,5,6,7]
# print(arrayrotate(arr))

# video 2
def leftrotate(arr,k):
    k  = k%len(arr)
        
    def reverse(left,right):
        while left<right:
            arr[left],arr[right] = arr[right],arr[left]
            left+=1
            right-=1
            
    reverse(0,len(arr)-1)
    print(arr)
    reverse(0,k-1)
    print(arr)
    reverse(k,len(arr)-1) 
    print(arr) 

arr = [1,2,3,4,5,6,7]
k = 3
leftrotate(arr,k)
print(arr)