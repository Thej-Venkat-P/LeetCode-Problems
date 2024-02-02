# url: https://leetcode.com/problems/sequential-digits/


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        nums = "123456789"
        l = len(str(low))
        h = len(str(high))
        ans = []

        for i in range(l, h + 1):
            for j in range(10 - i):
                sub = int(nums[j : j + i])
                if sub in range(low, high + 1):
                    ans.append(sub)

        return ans
