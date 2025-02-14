def commonElements(arr1, arr2, arr3):
        sarr1 = set(arr1)
        sarr2 = set(arr2)
        sarr3 = set(arr3)
        x = sarr1.intersection(sarr2).intersection(sarr3)
        x= sorted(x)
        
        return x if x else [-1]

sarr1 = [1, 5, 10, 20, 40, 80] 
sarr2 = [6, 7, 20, 80, 100]
sarr3 = [3, 4, 15, 20, 30, 70, 80, 120]
print(commonElements(sarr1, sarr2, sarr3))