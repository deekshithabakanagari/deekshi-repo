def rat_count(r, unit, arr):
    total_food = r * unit
    result = 0
    food_eaten = 0
    for i in arr:
        food_eaten += i
        result += 1
        if food_eaten > total_food:
            return result
    return 0

print(rat_count(7, 2, [2, 8, 3, 5, 7, 4, 1, 2]))