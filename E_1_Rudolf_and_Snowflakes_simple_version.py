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
def build_spf(mx):
    spf = [0] * mx
    primes = []
    
    for i in range(2, mx):
        if spf[i] == 0:
            spf[i] = i
            primes.append(i)
        
        for p in primes:
            if p > spf[i] or i * p >= mx:
                break
            spf[i * p] = p
    
    return spf

def factorize(x, spf):
    res = []
    while x > 1:
        res.append(spf[x])
        x //= spf[x]
    return res

def get_prime_factors_with_exp(x, spf):
    pf = {}
    while x > 1:
        p = spf[x]
        pf[p] = pf.get(p, 0) + 1
        x //= p
    return pf

def get_divisors(x, spf):
    pf = get_prime_factors_with_exp(x, spf)
    divisors = [1]
    
    for p, exp in pf.items():
        new_divs = []
        for d in divisors:
            val = 1
            for _ in range(exp + 1):
                new_divs.append(d * val)
                val *= p
        divisors = new_divs
    
    return divisors

# Example:
mx = 10**6
spf = build_spf(mx)
# print(factorize(100, spf))
# print(get_divisors(100, spf))


def solution(_):
    n = read_int()
    
    divisors = get_divisors(n-1, spf)
    
    for k in divisors:
        
    
    for k in range(2, int(n**0.5) + 2):
        cur = 1
        total = 1
        
        while total < n:
            cur *= k
            total += cur
        
        if total == n and cur >= k * k:
            yn(1)
            return
    
    yn(0)

































def main():
    t = 1
    t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()