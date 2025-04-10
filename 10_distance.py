def get_distance(x1, y1, x2, y2, x3, y3):
    
    def calc_dist(x1, y1, x2, y2):
        return round(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5, 2)
    
    d1 = calc_dist(x1, y1, x2, y2)
    d2 = calc_dist(x2, y2, x3, y3)
    d3 = calc_dist(x3, y3, x1, y1)

    return d1 + d2 + d3

print(get_distance(1, 1, 2, 4, 3, 6))