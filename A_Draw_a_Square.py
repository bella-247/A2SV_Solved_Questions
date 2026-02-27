for _ in range(int(input())):
    l, r, d, u = list(map(int, input().split()))
    
    if l == r and r == d and d == u:
        print("YES")
    else:
        print("NO")