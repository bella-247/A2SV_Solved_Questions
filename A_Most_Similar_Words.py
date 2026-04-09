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
F = lambda c : ord(c) - ord("a")

def difference(x, y):
    m = len(x)
    
    total = 0
    
    for i in range(m):
        total += abs(F(x[i]) - F(y[i]))
        
    return total

def solution(_):
    n, m = read_ints()
    words = [input().strip() for _ in range(n)]
    
    smallest_difference = difference(words[0], words[1])
    
    for i in range(n):
        for j in range(i + 1, n):
            diff = difference(words[i], words[j])
            if diff < smallest_difference:
                smallest_difference = diff 
                
    print(smallest_difference)
    








def main():
    t = 1
    t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()