def mismatches(matrix, top, right, bottom, left):
    size = right - left + 1

    if size <= 1:
        return 0
   
    top_side = [matrix[top][i] for i in range(left + 1, right)]
    right_side = [matrix[i][right] for i in range(top + 1, bottom)]
    bottom_side = [matrix[bottom][i] for i in range(right - 1, left, -1)]
    left_side = [matrix[i][left] for i in range(bottom - 1, top, -1)]
    
    # we do the corners alone, so that they won't be counted 
    summ = matrix[top][left] + matrix[top][right] + matrix[bottom][left] + matrix[bottom][right]
    
    # minimum required cell changes
    count = (2 if summ == 2 else summ % 2)
    
    for i in range(size - 2):
        summ = top_side[i] + left_side[i] + bottom_side[i] + right_side[i]
        count += (2 if summ == 2 else summ % 2)
    
    return count + mismatches(matrix, top + 1,right - 1, bottom - 1, left + 1)
    
for _ in range(int(input())):
    n = int(input())
    grid = [list(map(int, list(input()))) for __ in range(n)]
        
    print(mismatches(grid, 0, n - 1, n - 1, 0))
    
    

    