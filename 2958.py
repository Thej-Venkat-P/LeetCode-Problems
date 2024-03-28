# url: https://leetcode.com/problems/maximum-equal-frequency/


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = collections.defaultdict(int)
        start = 0
        ans = 1
        for end in range(len(nums)):
            freq[nums[end]] += 1
            while freq[nums[end]] > k:
                freq[nums[start]] -= 1
                start += 1
            if end - start + 1 > ans :
                ans = end - start + 1
        return ans