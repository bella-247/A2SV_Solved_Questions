from collections import defaultdict, deque, Counter
import math
import sys
import bisect
import itertools

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
    n = read_int()
    s = input().strip()
    
    total = {
        "L" : s.count("L"),
        "O" : s.count("O")
    }
    
    window = {"L" : 0, "O" : 0}
    
    for right in range(n-1):
        window[s[right]] += 1
        
        right_window = {
            "L" : total["L"] - window["L"],
            "O" : total["O"] - window["O"],
        }
        if window["L"] != right_window["L"] and window["O"] != right_window["O"]:
            print(right + 1)
            return
        
        
    
    print(-1)
    return
        
    
        
        



































def main():
    t = 1
    # t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()