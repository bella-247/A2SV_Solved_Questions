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
    n, a, b, k = read_ints()
    nums = read_list()
    
    def calc(health):
        two = a + b
        rounds = math.ceil(health / two)
        health -= (rounds - 1) * two
        health -= a

        needed_rounds = math.ceil(health / a)
        return needed_rounds
    
    nums.sort(key=lambda health: calc(health))
    
    total = 0
    for health in nums:
        taken_rounds = calc(health)
        
        if taken_rounds <= k:
            k -= taken_rounds
            total += 1

    print(total)
            
            
        
        
        
            
    
    
    



































def main():
    t = 1
    # t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()

