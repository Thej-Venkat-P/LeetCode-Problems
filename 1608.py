# url: https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        prev = -float('inf')
        for i in range(n):
            if n - i <= nums[i] and n - i > prev:
                return n - i
            prev = nums[i]
        return -1