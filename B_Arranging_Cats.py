for _ in range(int(input())):

    n = int(input())
    s = input()
    f = input()

    # print(s)

    count10 = 0
    count01 = 0

    for i in range(n):
        if s[i] == f[i]:
            continue
        
        if s[i] == "1" and f[i] == "0":
            count10 += 1
            
        elif s[i] == "0" and f[i] == "1":
            count01 += 1
            
            
    minn = min(count10, count01)
    count10 -= minn
    count01 -= minn
        
    print(minn + count10 + count01)