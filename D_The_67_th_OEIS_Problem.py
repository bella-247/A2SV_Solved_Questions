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
limit = 10 ** 10

def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    
    primes = [i for i in range(limit + 1) if is_prime[i]]
    return primes


primes = sieve(200000)

def solution(_):
    n = int(input())
    
    a = []
    for i in range(n):
        a.append(primes[i] * primes[i + 1])
    
    print(*a)


def main():
    t = 1
    t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()