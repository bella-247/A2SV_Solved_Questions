from collections import Counter

n = int(input())
nums = list(map(int, input().split()))
counts = [0] * 2001
place = 1
rating_place = Counter()

for num in nums:
    counts[num] += 1

for i in range(len(counts) - 1, -1, -1):
    if counts[i] == 0 or i in rating_place:
        continue
    
    rating_place[i] = place
    place += counts[i]
    
for num in nums:
    print(rating_place[num], end = " ")