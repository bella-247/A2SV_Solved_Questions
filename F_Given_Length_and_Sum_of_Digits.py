m, s = map(int, input().split())
if s == 0:
    if m == 1:
        print(0, 0)
    else:
        print(-1, -1)

elif 9 * m < s:
    print(-1, -1) 

else:
    # use as many 9's as possible and make the rest of the digits remainder 
    max_ = []
    max_.extend([9] * (s // 9))
    if s % 9 != 0:
        max_.append(s % 9)
    diff = m - len(max_)

    if diff > 0:
        for _ in range(diff):
            max_.append(0)

    min_ = max_[::-1]
    if min_[0] == 0:
        i = 1
        while min_[i] == 0:
            i += 1
        
        min_[0] = 1
        min_[i] -= 1

    max_ = "".join(map(str, max_))
    min_ = ''.join(map(str, min_))
    print(min_, max_)
