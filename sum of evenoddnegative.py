def sum_even_odd_negative(l):
    even_sum = 0
    odd_sum=0
    negative_sum=0
    for i in l:
        if i>0:
            if i%2==0:
                even_sum+=i
            elif i%2==1:
                odd_sum+=i
        else:
            negative_sum+=i
    return even_sum,odd_sum,negative_sum

l=[-12,34,35,89]
print(sum_even_odd_negative(l))