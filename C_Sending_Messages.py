for _ in range(int(input())):
    n, f, a, b = map(int, input().split())
    messages = list(map(int, input().split()))
    
    charge = f
   
    cost = min(messages[0] * a, b)
    charge -= cost
    
    if charge <= 0:
        print("NO")
        continue
    
    for i in range(1, n):
        distance = messages[i] - messages[i - 1]
        cost = min(distance * a, b)
        charge -= cost
        
        if charge <= 0:
            print("NO")
            break
        
    else:
        print("YES")
        