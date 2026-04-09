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
    s = input().strip()

    stack = [-1]
    longest = 0
    count = 0

    for i, c in enumerate(s):

        if c == "(":
            stack.append(i)

        else:
            stack.pop()

            if not stack:
                stack.append(i)

            else:
                length = i - stack[-1]

                if length > longest:
                    longest = length
                    count = 1

                elif length == longest:
                    count += 1

    if longest == 0:
        print(0, 1)
    else:
        print(longest, count)


def main():
    t = 1
    # t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()