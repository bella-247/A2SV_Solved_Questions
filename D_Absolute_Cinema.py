for _ in range(int(input())):
    n = int(input())
    results = list(map(int, input().split()))
    answer = [0] * n
    
    for i in range(1, n-1):
        x, y, z = results[i - 1], results[i], results[i + 1]
        answer[i] = (x + z - 2 * y) // 2
        
        
    left_middle_sum = 0
    right_middle_sum = 0
    for i in range(1, n - 1):
        left_middle_sum += (answer[i] * i)
        right_middle_sum += (answer[n - i - 1] * i)
        
        
    answer[0] = (results[-1] - right_middle_sum) // (n - 1)
    answer[n-1] = (results[0] - left_middle_sum) // (n - 1)
    
    print(*answer)