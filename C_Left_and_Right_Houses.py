import math

t = int(input())

for _ in range(t):
    n = int(input())
    nums = input()
    index = n

    zeros = nums.count("0")
    ones = n - zeros

    seen_counts = {"0": 0, "1": 0}

    for i in range(n):
        seen_counts[nums[i]] += 1
        left_zeros = seen_counts["0"]
        left_ones = seen_counts["1"]
        right_zeros = zeros - left_zeros
        right_ones = ones - left_ones

        left_satisfied = left_zeros
        right_satisfied = right_ones
        
        left_houses = i + 1
        right_houses = n - left_houses

        if left_satisfied >= math.ceil(left_houses / 2) and right_satisfied >= math.ceil(right_houses / 2):
            middle = n / 2 
            previous_distance = abs(middle - index)
            current_distance = abs(middle - i + 1)
            if current_distance < previous_distance:
                if _ == 6:
                    print("num", nums[i], i)
                    print(middle, index, i + 1, current_distance, previous_distance)
                index = i + 1

    print(index)
