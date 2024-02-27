# url: https://leetcode.com/problems/longest-consecutive-sequence/


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0
        for num in s:
            if num - 1 not in s:
                c = 0
                while num + c in s:
                    c += 1
                ans = max(ans, c)
        return ans