# url: https://leetcode.com/problems/first-missing-positive/


# Nums[i] contains both the number of occurences of i as n//i and the value at nums[i] as n%i.
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)
        n = len(nums)
        for i in range(n):
            if nums[i] not in range(1,n):
                nums[i] = 0
        print(nums)
        for i in range(n):
            index = nums[i] % n
            nums[index] += n
        for i in range(1,n):
            if nums[i] < n:
                return i
        return n


# Cycle sort

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(len(nums)):
            val = nums[i]
            while val > 0 and val <= n and val != i + 1 and val != nums[val - 1]:
                nums[i],nums[val - 1] = nums[val - 1],nums[i]
                val = nums[i]
        for i,num in enumerate(nums):
            if num != i+1:
                return i+1
        return n + 1