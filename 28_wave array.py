def wave(arr):
    for i in range(0, len(arr) - 1, 2):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr
arr = [1,2,3,4,5,6]
print(wave(arr))


def wave(arr):
    for i in range(1, len(arr) - 1, 2):
        arr[i], arr[i - 1] = arr[i - 1], arr[i]
    return arr
arr = [1,2,3,4,5]
print(wave(arr))

tc:O(n)
sc:O(1)