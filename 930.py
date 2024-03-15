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


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        i = 0
        ans = 0
        count = 0
        for j in range(len(nums)):
            if nums[j] == 1:
                goal -= 1
                count = 0
            while goal == 0 and i <= j:
                goal += nums[i]
                count += 1
                i += 1
            while goal < 0:
                goal += nums[i]
                i += 1
            ans += count
        return ans