for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    result = []
    changed = True
    while changed:
        changed = False
        for i in range(1, n):
            if a[i] < a[i-1]:
                a[i], a[i-1] = a[i-1], a[i]
                result.append([1, i])
                changed = True
                
    changed = True
    while changed:
        changed = False
        for i in range(1, n):
            if b[i] < b[i-1]:
                b[i], b[i-1] = b[i-1], b[i]
                result.append([2, i])
                changed = True
            
    for i in range(n):
        if a[i] > b[i]:
            result.append([3, i+1])
            a[i], b[i] = b[i], a[i]

    print(len(result))
    for i in range(len(result)):
        print(*result[i])