n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

cur = a[0]
count = 0
total = 0

j = 0
for i in range(n):
    if a[i] != cur:
        cur = a[i]
        count = 0

    # ignore the small ones
    while j < m and b[j] < cur:
        j += 1
    
    # count equal ones
    while j < m and b[j] == cur:
        j += 1
        count += 1
        
    total += count

print(total)