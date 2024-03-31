# url: https://leetcode.com/problems/count-number-of-nice-subarrays/


# Youtube Video Explanation: https://www.youtube.com/watch?v=Bk-HxzaooqM
# Optimized version
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        badi, maxi, mini = -1, -1, -1 
        ans = 0
        # -1 means not found
        for i, num in enumerate(nums):
            if not (minK <= num <= maxK):
                badi, maxi, mini = i, -1, -1
            if num == minK:
                mini = i
            if num == maxK:
                maxi = i

            if maxi > -1 and mini > -1:
                ans += min(mini, maxi) - badi

        return ans
