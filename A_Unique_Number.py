from collections import defaultdict, deque, Counter
import math
import sys
import bisect
import itertools
from unicodedata import numeric

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
    x = read_int()
    
    if x > 45:
        print(-1)
        return
    
    for i in range(1, 9 + 1):
        if x == i:
            print(i)
            return
    
    numbers = [9]

    summ = 9
    cur = 1
    while len(numbers) <= 9 and summ + cur <= 45:
        if cur >= numbers[-1]:
            summ += cur - 1
            numbers.append(cur - 1)
            cur = 1
        
        if summ + cur == x:
            number = str(cur) + "".join(map(str, numbers[::-1]))
            print(number)
            return
            
        cur += 1
        
        # print(str(cur) + "".join(map(str, numbers[::-1])))
            
            
    print(-1)
    return
        
    



































def main():
    t = 1
    t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()