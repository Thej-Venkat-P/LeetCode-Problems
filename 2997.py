# url: https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xs = 0
        for val in nums:
            xs ^= val
        
        xs ^= k
        return bin(xs).count('1')