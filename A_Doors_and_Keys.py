t = int(input())

for _ in range(t):
    s = input()
    seen = set()
    
    for c in s:
        if c.isupper() and c.lower() not in seen:
            print("NO")
            break

        seen.add(c.lower())

    else:
        print("YES")
        