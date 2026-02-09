from collections import Counter

for _ in range(int(input())):
    s = input()
    n = len(s)
    
    counts = Counter()
    
    for i in range(n):
        if i < n - 1 and s[i] in "*>" and s[i + 1] in "*<":
            print(-1)
            break
        else:
            counts[s[i]] += 1
            
    else:
        print(max(counts["<"], counts[">"]) + counts["*"])
