# url: https://leetcode.com/problems/binary-subarrays-with-sum/


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def max_occ(goal):
            if goal < 0:
                return 0
            l = 0
            c = 0
            ans = 0
            for r in range(len(nums)):
                c += nums[r]
                while c > goal:
                    c -= nums[l]
                    l += 1
                ans += r - l + 1
            return ans 
        return max_occ(goal) - max_occ(goal - 1)