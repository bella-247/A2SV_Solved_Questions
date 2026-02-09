from collections import Counter
from heapq import heapify, heappush, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        max_heap = []
        for num, count in counts.items():
            heapq.heappush(max_heap, (-count, num))

        # Extract the top k frequent elements
        result = []
        for _ in range(k):
            count, num = heapq.heappop(max_heap)
            result.append(num)

        return result
