def largest_even_odd(l):

    largest_even = float('-inf')
    largest_odd = float('-inf')
    for i in l:
        if i%2==0 and i>largest_even:
            largest_even=i
        elif i%2==1 and i>largest_odd:
            largest_odd=i
    return largest_even,largest_odd

l=[3,4,5,6,7]
print(largest_even_odd(l))
    
