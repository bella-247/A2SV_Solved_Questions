import math

def distance(x1, y1, x2, y2):
    x = (x1 - x2) ** 2
    y = (y1 - y2) ** 2
    
    return math.sqrt(x + y)

for _ in range(int(input())):
    corners = [list(map(int, input().split())) for __ in range(4)]
    corners.sort()
    
    area = distance(*corners[0], *corners[1]) * distance(*corners[2], *corners[3])

    print(int(area))
    
    
    