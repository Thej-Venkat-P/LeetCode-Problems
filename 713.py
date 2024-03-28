# url: https://leetcode.com/problems/subarray-product-less-than-k/


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        n = len(nums)
        start = 0
        prod = 1
        ans = 0
        for end in range(n):
            prod *= nums[end]
            while prod >= k and start <= end:
                prod /= nums[start]
                start += 1
            ans += end - start + 1
        return ans