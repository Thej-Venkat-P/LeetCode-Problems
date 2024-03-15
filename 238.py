# url: https://leetcode.com/problems/product-of-array-except-self/


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        curr = 1
        for i in range(n):
            ans[i] = curr
            curr *= nums[i]
        curr = 1
        for i in range(n-1, -1, -1):
            ans[i] *= curr
            curr *= nums[i]
        return ans
    
    
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_prod = 1
        suf_prod = 1
        num_len = len(nums)
        pre_l = [1] * num_len
        suf_l = [1] * num_len
        res = [1] * num_len

        for i in range(num_len):
            pre_l[i] = pre_prod
            pre_prod *= nums[i]

        for j in range(num_len-1, -1, -1):
            suf_l[j] = suf_prod
            suf_prod *= nums[j]

        for i in range(num_len):
            res[i] = pre_l[i] * suf_l[i]

        return res