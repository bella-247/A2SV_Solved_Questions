def solution():
    n, s = map(int, input().split())
    nums = list(map(int, input().split()))

    count = 0
    
    window = 0
    left = 0
    for right in range(n):
        while left <= right and window < s:
            pass
        
    return count



















for _ in range(int(input())):
    result = solution()
    if isinstance(result, bool):
       print('YES' if result else 'NO')
    elif isinstance(result, list):
       print(*result)
    elif isinstance(result, tuple):
       print(*result)
    else:
       print(result)
