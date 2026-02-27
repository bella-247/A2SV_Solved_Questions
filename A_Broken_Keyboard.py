for _ in range(int(input())):
    s = input()
    n = len(s)

    result = set()

    i = 0
    while i < n:
        char = s[i]
        count = 0
        while i < n and s[i] == char:
            count += 1
            i += 1
        
        if count % 2 != 0 and char not in result:
            result.add(char)
        
    print("".join(sorted(result)))