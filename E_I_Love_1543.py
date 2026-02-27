def countPattern(circular, pattern):
    n = len(circular)
    k = len(pattern)
    extended = circular + circular[:k-1]
    return sum(1 for i in range(n) if extended[i:i+k] == pattern)

def extractCirculars(grid, n, m):
    size = n * m
    top, right, bottom, left, = 0, m - 1, n - 1, 0
    
    circulars = []
    
    while size >= 4:
    
        circular = []
    
        # left to right (at the top)
        for i in range(left, right):
            circular.append(grid[top][i])
            
        # top to bottom (at the right)
        for i in range(top, bottom):
            circular.append(grid[i][right])
            
        # right to left (at the bottom)
        for i in range(right, left, -1):
            circular.append(grid[bottom][i])
        
        # bottom to top (at the left)
        for i in range(bottom, top, -1):
            circular.append(grid[i][left])

        top = top + 1
        right = right - 1
        bottom = bottom - 1
        left = left + 1
        size = (bottom - top + 1) * (right - left + 1)
        
        circulars.append(circular)
        
    return circulars

for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    grid = [list(input()) for _ in range(n)]
    
    circulars = extractCirculars(grid, n, m)

    total = 0
    for circular in circulars:
        total += countPattern(circular, ['1', '5', '4', '3'])
        
    print(total)