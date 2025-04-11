# This completely runs on a formula
# 30 x H - 5.5 x M

def get_angle(h, m):
    
    # Setting hour and minute
    if m == 60:
        m = 0
        h += 1
    h = h % 12

    # The distances travelled by the hands
    hour = (h * 60 + m) * 0.5
    minute = 6 * m

    # Calc and returning the angles
    angle = abs(hour - minute)
    return min(angle, 360 - angle)

h = 9
m = 60
print(get_angle(h, m))