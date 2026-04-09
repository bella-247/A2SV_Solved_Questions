from collections import defaultdict, deque, Counter
import math
import sys
import bisect
import itertools

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
    boys = read_list()
    boys.sort()
    
    boys_count = Counter(boys)
    
    m = read_int()
    girls = read_list()
    girls.sort()
    
    girls_count = Counter(girls)
    
    count = 0
    
    for girl in girls:
        need1 = girl - 1
        need2 = girl
        need3 = girl + 1
        
        if need1 in boys_count:
            count += 1
            boys_count[need1] -= 1
            
            if boys_count[need1] == 0:
                del boys_count[need1]
            
        elif need2 in boys_count:
            count += 1
            boys_count[need2] -= 1
            
            if boys_count[need2] == 0:
                del boys_count[need2]
                
        elif need3 in boys_count:
            count += 1
            boys_count[need3] -= 1
            
            if boys_count[need3] == 0:
                del boys_count[need3]
            

    print(count)    
    
    
    

    
    


































def main():
    t = 1
    # t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()