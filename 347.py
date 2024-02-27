# Url: https://leetcode.com/problems/top-k-frequent-elements/


import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        counts = collections.Counter(nums)
        for unique_num in counts:
            if len(heap) < k:
                heapq.heappush(heap, (counts[unique_num], unique_num))
            elif counts[unique_num] > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (counts[unique_num], unique_num))
        return [ elem[1] for elem in heap ]