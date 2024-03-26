# url: https://leetcode.com/problems/first-missing-positive/


class Solution:
    # Nums[i] contains both the number of occurences of i as n//i and the value at nums[i] as n%i.
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0) # To handle the case where n is present in nums, we need to have n+1 elements in nums.
        l = len(nums)

        for i, n in enumerate(nums):
            if n not in range(1, l):
                nums[i] = 0

        for i, n in enumerate(nums):
            if n%l != 0:
                nums[n % l] += l

        for i,n in enumerate(nums[1:]):
            if n < l:
                return i + 1

        return l

    # Swapping till we get correct index for each element.
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        for i, num in enumerate(nums):
            while 1<=num<=n and num != nums[num - 1]:
                nums[i], nums[num - 1] = nums[num - 1], nums[i]
                num = nums[i]

        for i in range(n):
            if nums[i] != i+1:
                return i+1

        return n + 1