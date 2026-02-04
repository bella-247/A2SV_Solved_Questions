from collections import Counter
t = int(input())

for _ in range(t):
    s = input()
    t = input()
    
    dic1 = Counter(s)
    dic2 = Counter(t)
    
    if any(dic1[key] > dic2[key] for key in dic1):
        print("Impossible")
        continue
    
    result = []
    i = 0
    dic2 = sorted(dic2.items())
    for char, freq in dic2:
        diff_count = freq - dic1[char]
        
        while i < len(s) and s[i] <= char:
            result.append(s[i])
            i += 1
        
        result.append(char * diff_count)
        
    result.append(s[i:])
    print("".join(result))
    