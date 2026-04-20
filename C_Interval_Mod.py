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
# iinf = 10 ** 18 + 1
# MOD = 10**9 + 7
def solution(_):
    n, k, p, q = read_ints()
    nums = read_list()

    # result = []
    
    totalP = 0
    totalQ = 0
    
    for i in range(k):
        totalP += nums[i] % p % q
        totalQ += nums[i] % q % p
    
    smallestP_sum = totalP
    smallestP = [0, k - 1]
    
    left = 0
    for right in range(k,n):
        totalP += (nums[right] % p % q)
        totalP -= (nums[left] % p % q)
        
        if totalP < smallestP_sum:
            smallestP[0] = left 
            smallestP[1] = right
            
        left += 1
    
    smallestQ_sum = totalQ
    smallestQ = [0, k - 1]
    
    left = 0
    for right in range(k,n):
        totalP += (nums[right] % q % p)
        totalP -= (nums[left] % q % p)
        
        if totalQ < smallestQ_sum:
            smallestQ[0] = left 
            smallestQ[1] = right
            
        left += 1
    
    left, right = smallestQ if smallestQ_sum < smallestP_sum else smallestP

    total = min(smallestP_sum, smallestQ_sum)
    
    for i in range(n):
        if left <= i <= right:
            continue
        
        total += min(nums[i] % p % q, nums[i] % q % p)
        
    print(total)
    
    
        


def main():
    t = 1
    t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()