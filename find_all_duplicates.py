from typing import List
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)
        
        i = 0
        while i < n:

            while nums[i] != i + 1:
                print(nums[i], i + 1)
                num = nums[i]
                cor_pos = num - 1

                if nums[cor_pos] == num:
                    result.append(num)
                    print(result, nums)
                    break
                
                else:
                    nums[i], nums[cor_pos] = nums[cor_pos], nums[i]
            i += 1

        return result
    
    
s = Solution()
print(s.findDuplicates([4,3,2,7,8,2,3,1]))

    