def split_even_odd(l):
    even_list = []
    odd_list=[]
    for i in l:
        if i%2==0:
            even_list.append(i)
        else:
            odd_list.append(i)
    return even_list,odd_list
l=list(map(int,input().split()))
print(split_even_odd(l))
