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
# iinf = 10 ** 18 + 1
# MOD = 10**9 + 7
def solution(_):
    s = input().strip()
    n = len(s)
    
    prefix = [0] * (n + 1)
    mapp = defaultdict(int)
    
    for i in range(n):
        prefix[i] = prefix[i - 1] + (1 if s[i] == "-" else -1)
        init = prefix[i] - 1
        
        if init not in mapp:
            mapp[init] = i + 1

    number = max(prefix)
    mapp[number] = n    

    total = 0
    
    for i in range(number + 1):
        total += mapp[i] 
    
    print(total)

            
        
        



































def main():
    t = 1
    t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()