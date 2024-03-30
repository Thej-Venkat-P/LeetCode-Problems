# url: https://leetcode.com/problems/subarrays-with-k-different-integers/


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        unique_count = 0
        counts = {}
        left_far = left_near = 0
        res = 0

        for right in range(len(nums)):
            if nums[right] not in counts:
                unique_count += 1
                counts[nums[right]] = 1
            else:
                counts[nums[right]] += 1
            
            if unique_count > k :
                while counts[nums[left_near]] != 1 :
                    counts[nums[left_near]] -= 1
                    left_near += 1
                del counts[nums[left_near]]
                left_near += 1
                left_far = left_near
                unique_count -= 1
            
            if unique_count == k :
                while counts[nums[left_near]] > 1:
                    counts[nums[left_near]] -= 1
                    left_near += 1
                res += left_near - left_far + 1
        
        return res

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def f(counts=[0] * (len(nums) + 1), low=0, high=0, k=k):
            for num in nums:
                if not counts[num]:
                    if (k := k - 1) < 0:
                        counts[nums[high]] = 0
                        low = high = high + 1
                counts[num] += 1
                if k <= 0:
                    while counts[(a := nums[high])] > 1:
                        counts[a] -= 1
                        high += 1
                    yield high - low + 1

        return sum(f())  