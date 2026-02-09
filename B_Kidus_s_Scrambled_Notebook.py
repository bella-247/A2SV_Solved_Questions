for _ in range(int(input())):
    s = input()
    
    i = 1
    while i < len(s) and s[i] == "0":
        i += 1
    
    a = s[:i]
    b = s[i:]

    if b and int(b) > int(a):
        print(f"{a} {b}")
    else:
        print(-1)