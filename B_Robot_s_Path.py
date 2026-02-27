n, k = list(map(int, input().split()))
s = input()

i = 0
while i < n - 1:
    if s[i + 1] == ".":
        i += 1
        continue
    
    next_best = 0
    for j in range(1, k + 1):
        if i + j < n and s[i + j] == ".":
            next_best = j
            
    if next_best == 0:
        print("NO")
        break
    
    i += next_best
    
else:
    print("YES")