t = int(input())

for i in range(t):
    # if i < 3 or i >= 11:
        n = int(input())
        nums = list(map(int, input().split()))
        count = 0
        max_ = 0
        for num in nums:
            if num > 0:
                count += 1
                max_ = max(max_, num)
                
        print(count - (n - max_))
        