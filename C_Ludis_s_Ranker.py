n = int(input())
nums = list(map(int, input().split()))

sorted_nums = sorted(nums, reverse=True)
rating_place = {}
place_count = 1

for num in sorted_nums:
    if num in rating_place:
        place_count += 1
        continue
    
    rating_place[num] = place_count
    place_count += 1

for num in nums:
    print(rating_place[num], end = " ")