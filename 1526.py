# url: https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        count = prev = target[0]
        for num in target[1:]:
            if num > prev:
                count += num - prev
            prev = num
        return count
