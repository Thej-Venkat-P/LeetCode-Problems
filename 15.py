# url: https://leetcode.com/problems/3sum/


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        s = set()
        for i in range(n-2):
            num = -nums[i]
            if num < 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = i + 1, n - 1
            while j < k:
                d = nums[j] + nums[k]
                if d == num:
                    s.add((-num, nums[j], nums[k]))
                    k -= 1
                    j += 1
                elif d < num:
                    j += 1
                else:
                    k -= 1
        return list(s)
