def inverted_star_pattern(n):
    for i in range(n,0,-1):
        print(('* ' * i).center(2 * n-1))
n=int(input())                                  #-->ljust(),rjust(),center()
inverted_star_pattern(n)
