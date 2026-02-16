def yes_no(check):
    print("YES" if check else "NO")
    
for _ in range(int(input())):
    n = int(input())
    nums = set(map(int, input().split()))
    
    yes_no(67 in nums)