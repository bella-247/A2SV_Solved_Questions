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
    skills = read_list()
    damages = read_list()
    
    fires = [i for i in range(n) if skills[i] == 0]
    frosts = [i for i in range(n) if skills[i] == 1]
    
    fires.sort(reverse=True, key=lambda i: damages[i])
    frosts.sort(reverse=True, key=lambda i: damages[i])
    
    if len(fires) == 0 or len(frosts) == 0:
        total = 0
        for i in fires:
            total += damages[i]
        
        for i in frosts:
            total += damages[i]
        
        print(total)
        return
    
    total = 0
    common = min(len(fires), len(frosts)) - 1
    
    for i in range(common + 1):
        total += (2 * damages[fires[i]])
        total += (2 * damages[frosts[i]])
    
    minn = min(damages[fires[common]], damages[frosts[common]])
    
    if len(fires) == len(frosts):
        total -= minn
    
    for i in range(common + 1, len(fires)):
        total += damages[fires[i]]
    
    for i in range(common + 1, len(frosts)):
        total += damages[frosts[i]]
        
    print(total)


def main():
    t = 1
    t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()