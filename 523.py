# url: https://leetcode.com/problems/continuous-subarray-sum/


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder = {0:-1}
        presum = 0
        for i, num in enumerate(nums):
            presum += num
            r = presum % k
            if r in remainder:
                if i - remainder[r] >= 2:
                    return True
            else:
                remainder[r] = i
        return False