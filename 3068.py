from heapq import heapify, heappush, heappop
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        xor_val = [num ^ k for num in nums]
        n = len(nums)
        diff = []
        for i in range(n):
            heappush(diff, nums[i] - xor_val[i])
        s = sum(nums)
        while diff:
            top = -heappop(diff)
            if not diff:
                break
            if top - diff[0] <= 0:
                break
            second = -heappop(diff)
            s += top + second
        return s
    
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        min_diff = float('inf')
        even_count = True
        res = 0

        for num in nums:
            diff = (num^k) - num
            if diff > 0:
                even_count = not even_count
                if diff < min_diff:
                    min_diff = diff
                res += num^k
            else:
                if -diff < min_diff:
                    min_diff = -diff
                res += num
                
        if not even_count:
            res -= min_diff
        return res