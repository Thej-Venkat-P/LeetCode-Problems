# url: https://leetcode.com/problems/sort-colors/


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        n = len(nums)
        for j in range(n):
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        for j in range(i, n):
            if nums[j] == 1:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
        

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l, r = 0, len(nums) - 1
        m = 0
        while m <= r:
            if nums[m] == 0:
                nums[m], nums[l] = nums[l], nums[m]
                m += 1
                l += 1
            elif nums[m] == 1:
                m += 1
            else:
                nums[m], nums[r] = nums[r], nums[m]
                r -= 1
        