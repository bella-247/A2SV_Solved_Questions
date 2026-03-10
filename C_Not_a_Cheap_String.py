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

ORD = lambda char : ord(char) - ord("a") + 1
def calcPrice(s):
    if not s:
        return 0
    
    return sum(ORD(c) for c in s)

def solution():
    w = input().strip()
    p = read_int()
    
    price = calcPrice(w)
    if  price <= p:
        print(w)
        return
    
    result = list(w)
    positions = defaultdict(list)
    
    for i, char in enumerate(w):
        positions[char].append(i)

    sorted_positions = sorted(positions, reverse=True)
    i = 0
    while price > p:
        char = sorted_positions[i]
        
        if len(positions[char]) > 0:
            index = positions[char].pop()
            price -= ORD(char)
            
            result[index] = ""
            
        else:
            i += 1
        
    print("".join(result))


def main():
    t = 1
    t = int(read_int())
    for _ in range(t):
        solution()

if __name__ == "__main__":
    main()