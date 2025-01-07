def merge_sort(nums1,nums2):
    result=[]
    n1=n2=0

    while n1<len(nums1)     and      n2 < len(nums2):
        if nums1[n1]   <     nums2[n2]:
            result.append(nums1[n1])
            n1+=1
        else:
            result.append(nums2[n2])
            n2+=1
     
    while n1<len(nums1):
        result.append(nums1[n1])
        n1+=1

    while n2<len(nums2):
        result.append(nums2[n2])
        n2+=1
    
    return result

nums1=[10,20,35,55,71]
nums2=[5,37]
print(merge_sort(nums1,nums2))