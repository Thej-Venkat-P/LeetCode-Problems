# url: https://leetcode.com/problems/minimum-increment-to-make-array-unique


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        count = Counter(nums)
        n = len(nums)
        if len(count) == n:
            return 0

        moves = 0
        prev = 0
        keys = sorted(count.keys())
        for key in keys:
            while count[key] > 1:
                prev = max(prev, key + 1)
                while prev in count:
                    prev += 1
                moves += prev - key
                count[key] -= 1
                count[prev] = 1
        return moves

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        dp = [0]*(max(nums) + 1)
        for num in nums:
            dp[num] += 1
        
        moves = 0
        for i in range(len(dp) - 1):
            val = dp[i]
            if val > 1:
                moves += val - 1
                dp[i + 1] += val - 1
        val = dp[-1] - 1
        moves += (val * (val + 1)) // 2

        return moves