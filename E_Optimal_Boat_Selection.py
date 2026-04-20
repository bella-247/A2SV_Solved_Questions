from collections import defaultdict, deque, Counter
import math, sys, bisect, itertools

# sys.setrecursionlimit(10**7)
input = sys.stdin.readline


def print(*args, **kwargs):
    sys.stdout.write(" ".join(map(str, args)) + kwargs.get("end", "\n"))


def read_int():
    return int(input().strip())


def read_ints():
    return map(int, input().split())


def read_list():
    return list(map(int, input().split()))


def yn(res):
    print("YES" if res else "NO")


inf = float("inf")


# iinf = 10 ** 18 + 1
# MOD = 10**9 + 7
def solution(_):
    n, v = read_ints()
    nums = [[*read_list(), i] for i in range(n)]

    print(nums)
    nums.sort()
    
    space = 0

    caps = defaultdict(list)
    indices = defaultdict(list)
    
    for t, c, index in nums:
        caps[t].append(c)
        caps[t].append(index)
        
    taken = []
    
    while len(taken) <= n and space > 0:
        one = caps[1][-1] if len(caps[1]) >= 1 else None
        one_one = sum(caps[1][-2:]) if len(caps[1]) else None
        two = caps[2][-1] if len(caps[2]) >= 1 else None
        one_two = one + two if one and two else None
        

        if space == 1:
            if not one:
                break
            
            caps[1].pop()
            index = indices[1].pop()
            taken.append(index)
            break
        
        elif space == 2:
            one = one_one or one
            
            if not one:
                caps[2].pop()
                index = indices[2].pop()
                taken.append(index)
                
            elif not two:
                index1 = index2 =  None
                
                caps[1].pop()
                index1 = indices[1].pop()
                if one_one: 
                    caps[1].pop()
                if one_one: 
                    index2 = indices[1].pop()
                
                taken.append(index1)
                if index2:
                    taken.append(index2)
                    
            # space 3 or more    
            else:
                
                
                
            
            


        
        
        
        
    capacity = 0
    for index in taken:
        capacity += nums[index][1]
        
        
    print(capacity)

















def main():
    t = 1
    # t = int(read_int())
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()
