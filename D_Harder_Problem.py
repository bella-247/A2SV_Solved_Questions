t = int(input())

for _ in range(t):
    n = int(input())
    total_range = set(range(1, n + 1))
    nums = list(map(int, input().split()))
    
    for num in nums:
        if num in total_range:
            print(num, end = " ")
            total_range.remove(num)
        
    for num in total_range:
        print(num, end = " ")

    print()
