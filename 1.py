# url: https://leetcode.com/problems/two-sum/


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, e in enumerate(nums):
            if target - e in d:
                return [d[target - e], i]
            d[e] = i
        return []


# O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in d:
                return [d[diff], i]
            d[nums[i]] = i
        return -1