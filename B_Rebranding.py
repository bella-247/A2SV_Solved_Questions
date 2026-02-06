from collections import defaultdict

n, m = list(map(int, input().split()))
s = list(input())

mapp = defaultdict(list)

for i in range(n):
    mapp[s[i]].append(i)

for _ in range(m):
    x, y = input().split()
    
    mapp[x], mapp[y] = mapp[y], mapp[x]
    
    if not mapp[x]:
        del mapp[x]
        
for char in mapp:
    indices = mapp[char]
    for index in indices:
        s[index] = char
        
print("".join(s))