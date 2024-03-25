# url: https://leetcode.com/problems/find-all-duplicates-in-an-array/


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = [num - 1 for num in nums]
        ans = []
        for num in nums:
            idx = num % n
            nums[idx] += n
        for i, num in enumerate(nums):
            if num // n > 1:
                ans.append(i + 1)
        return ans


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        for num in nums:
            val = nums[abs(num) - 1]
            if val < 0:
                ans.append(abs(num))
            else:
                nums[abs(num) - 1] *= -1
        return ans