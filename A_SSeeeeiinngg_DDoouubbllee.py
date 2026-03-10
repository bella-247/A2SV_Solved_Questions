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

# def isPalindrome(word):
#     i = 0
#     j = len(word) - 1
    
#     while i < j:
#         if word[i] != word[j]:
#             return False
        
#         i += 1
#         j -= 1
        
#     return True

def solution():
    s = input().strip()
    print(s + s[::-1])    




















def main():
    t = 1
    t = int(read_int())
    for _ in range(t):
        solution()

if __name__ == "__main__":
    main()