from collections import defaultdict, deque, Counter
import math, sys, bisect, itertools

# sys.setrecursionlimit(10**7)
input = sys.stdin.readline
def print(*args, **kwargs):
    sys.stdout.write(" ".join(map(str, args)) + kwargs.get("end", "\n"))

def read_int(): return int(input().strip())
def read_ints(): return map(int, input().split())
def read_list(): return list(map(int, input().split()))
def yn(res): print("YES" if res else "NO")

inf = float('inf')
MOD = 10**9 + 7
def solution(_):
    n, x = read_ints()
    
    vouchers = [read_list() for _ in range(n)]
    vouchers.sort(key=lambda v: (v[1], -v[2]))
    ans = inf
    
    diffs = defaultdict(list)
    costs = defaultdict(list)
    
    for start, end, cost in vouchers:
        diff = end - start + 1
        
        diffs[diff].append(end)
        
        min_cost = costs[diff][-1] if costs[diff] else inf
        
        costs[diff].append(min(cost, min_cost))

        
    for start, end, cost in vouchers:
        diff = end - start + 1
        need = x - diff
        
        if need not in diffs:
            continue
        
        group = diffs[need]
        
        index = bisect.bisect_left(group, start) - 1
        
        if index == -1:
            continue

        other_cost = costs[need][index]
        
        ans = min(ans, cost + other_cost)
        
        

    
    
    
    print(-1 if ans == inf else ans)





























def main():
    t = 1
    # t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()