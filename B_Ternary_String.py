from collections import defaultdict, deque, Counter
import math, sys, bisect, itertools

# sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()

def print(*args, **kwargs):
    sys.stdout.write(" ".join(map(str, args)) + kwargs.get("end", "\n"))

def ri():
    return int(input())

def ril():
    return list(map(int, input().split()))

def yn(res):
    print("YES" if res else "NO")


inf = float("inf")
iinf = 10**18 + 1


# MOD = 10**9 + 7
def solution(_):
    s = input()
    n = len(s)
    
    smallest = inf

    window = Counter()

    left = 0
    for right in range(n):
        window[s[right]] += 1

        while len(window) == 3:
            smallest = min(smallest, right - left + 1)
            window[s[left]] -= 1

            if window[s[left]] == 0:
                del window[s[left]]

            left += 1

    print(smallest if smallest < inf else 0)


def main():
    t = 1
    t = ri()
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()
