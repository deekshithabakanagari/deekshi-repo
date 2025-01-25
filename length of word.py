def larger_str(s):
    result=s[0]
    length = len(s[0])
    for i in s:
        if len(i)>length:
            length = len(i)
            result=i
    return result
        
s=["bangalore","chennai","andhra pradesh"]
print(larger_str(s))

    