t = int(input())

for _ in range(t):
    a, b, n = list(map(int, input().split()))
    tools = list(map(lambda x : min(int(x), a), input().split()))
    
    seconds = b + sum(min(n, a-1) for n in tools)
    
    print(seconds)
    