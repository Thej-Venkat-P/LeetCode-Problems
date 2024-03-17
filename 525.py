# url: https://leetcode.com/problems/contiguous-array/


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        c = 0
        diff = {0 : -1}
        ans = 0
        for i, n in enumerate(nums):
            if n == 1:
                c += 1
            else:
                c -= 1
            if c in diff:
                if i - diff[c] > ans:
                    ans = i - diff[c]
            else:
                diff[c] = i
        return ans