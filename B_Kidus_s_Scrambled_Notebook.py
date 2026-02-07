for _ in range(int(input())):
    s = input()
    a, b = int(s[0]), s[1:]
    
    i = 1
    while i < len(s) and s[i] == "0":
        a = a * 10
        b = b[1:]
        
        i += 1

    b = int(b) if b else 0

    if b > a:
        print(f"{a} {b}")
    else:
        print(-1)