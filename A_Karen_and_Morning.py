from collections import defaultdict, deque, Counter
import math
import sys
input = sys.stdin.readline

def isPalindrome(hour, minute):
    hour = str(hour).zfill(2)
    minute = str(minute).zfill(2)
    return hour == minute[::-1]

def solution():
    hour, minute = map(int, input().strip().split(":"))
    
    for i in range(1400):
        m = minute + i
        h = (hour + (m // 60)) % 24
        
        if isPalindrome(h, m % 60):
            print(i)
            break


t = 1
# t = int(input().strip())
for _ in range(t):
    solution()