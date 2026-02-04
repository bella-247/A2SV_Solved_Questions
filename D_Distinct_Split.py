from collections import Counter
t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    
    counts = Counter(s)
    left = set()
    maxx = len(counts)

    for c in s:
        left.add(c)
        counts[c] -= 1
        
        if counts[c] == 0:
            del counts[c]
            
        maxx = max(maxx, len(left) + len(counts))
        
    print(maxx)
    