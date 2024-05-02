# url: https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        ans = -1
        present = set(nums)
        for num in nums:
            if num > 0 and -num in present and num > ans:
                ans = num
        return ans