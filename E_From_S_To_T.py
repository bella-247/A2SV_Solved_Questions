from collections import Counter

for _ in range(int(input())):
    s, t, p = [input() for __ in range(3)]
    
    countS = Counter(s)
    countT = Counter(t)
    countP = Counter(p)
    
    # order
    i = 0
    for j in range(len(t)):
        if s[i] == t[j]:
            i += 1
        
        if i == len(s):
            break
    else:
        print("NO")
        continue
    
    # count
    for char, charCount in countT.items():
        if charCount > (countS[char] + countP[char]):
            print("NO")
            break
        
    else:
        print("YES")
        