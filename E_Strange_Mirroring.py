import math
# from math import ceil
t  = int(input())
for _  in range(t):
    s = input()
    q = int(input())
    queries = list(map(int, input().split()))
    ans = []


    for k in queries:
        if k <= len(s):
            app = s[k%len(s)-1]
            ans.append(app)
            continue

        count = 1
        step = math.ceil(math.log2(k/len(s)))
        prev_length = len(s) * (2 ** (step - 1))
        index = k % prev_length
        if index == 0:
            index = prev_length

        while index > len(s):
            count += 1
            step =  math.ceil(math.log2(index/len(s)))
            prev_length = len(s) * (2 ** (step - 1))
            index = index % prev_length

            if index == 0:
                index = prev_length

        
        app = s[index-1]

        if count % 2 == 0:
            ans.append(app)
        else:
            ans.append(app.swapcase())

    print(' '.join(ans))