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
    n = read_int()
    n = 2 ** n
    
    nums = read_list()
    
    indexed_nums = [[nums[i], i] for i in range(n)]

    def bisectLeft(arr, target):
        left = 0
        right = len(arr) - 1
        
        while left <= right:
            mid = left + (right - left ) // 2
            
            if arr[mid][0] >= target:
                right = mid - 1
                
            else:
                left = mid + 1
            
        return left
        
        
    def mergeSort(left, right, arr):
        wins = defaultdict(int)
        
        if left == right:
            return [arr[left]]
        
        mid = left + (right - left) // 2
        
        left_half = mergeSort(left, mid, arr)
        right_half = mergeSort(mid + 1, right, arr)
        
        for num, index in left_half:
            result = bisectLeft(right_half, num)
            wins[index] += result
        
        for num, index in right_half:
            result = bisectLeft(left_half, num)
            wins[index] += result

        for index, win in wins.items():
            indexed_nums[index][0] += win
            
        return sorted(left_half + right_half)
    
    mergeSort(0, n - 1, indexed_nums)
    print(*[indexed_nums[i][0] for i in range(n)])
        



































def main():
    t = 1
    t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()



# from collections import defaultdict, deque, Counter
# import math, sys, bisect, itertools

# # sys.setrecursionlimit(10**7)
# input = sys.stdin.readline
# def print(*args, **kwargs):
#     sys.stdout.write(" ".join(map(str, args)) + kwargs.get("end", "\n"))

# def read_int(): return int(input().strip())
# def read_ints(): return map(int, input().split())
# def read_list(): return list(map(int, input().split()))
# def yn(res): print("YES" if res else "NO")

# inf = float('inf')
# # iinf = 10 ** 18 + 1
# # MOD = 10**9 + 7
# def solution(_):
#     n = read_int()
#     n = 2 ** n
    
#     nums = read_list()
    
#     indexed_nums = [[nums[i], i] for i in range(n)]
    
#     def merge(left, right):
#         wins = defaultdict(int)
#         i =  j = 0
        
#         result = []
        
#         small_left = 0
#         small_right = 0
        
#         while i < len(left) and j < len(right):
            
#             if left[i][0] == right[j][0]:
#                 result.append(left[i])
#                 i += 1
                
#             elif left[i][0] < right[j][0]:
#                 small_left += 1
#                 wins[left[i][1]] = small_right
#                 result.append(left[i])
#                 i += 1
                
#             else:
#                 small_right += 1
#                 wins[right[j][1]] = small_left
#                 result.append(right[j])
#                 j += 1
                
#         while i < len(left):
#             wins[left[i][1]] = small_right
#             result.append(left[i])
#             i += 1
            
#         while j < len(right):
#             wins[right[j][1]] = small_left
#             result.append(right[j])
#             j += 1
            
            
#         for index, win in wins.items():
#             indexed_nums[index][0] += win

#         return result
        
        
#     def mergeSort(left, right, arr):        
#         if left == right:
#             return [arr[left]]
        
#         mid = left + (right - left) // 2
        
#         left_half = mergeSort(left, mid, arr)
#         right_half = mergeSort(mid + 1, right, arr)
        
#         return merge(left_half, right_half)
    
#     mergeSort(0, n - 1, indexed_nums)
#     print(*[indexed_nums[i][0] for i in range(n)])
        



































# def main():
#     t = 1
#     t = int(read_int())
#     for _ in range(t):
#         solution(_)

# if __name__ == "__main__":
#     main()