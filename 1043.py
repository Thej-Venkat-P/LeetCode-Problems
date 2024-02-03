# url: https://leetcode.com/problems/partition-array-for-maximum-sum/


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)
        for i in range(n):
            cur_sum = 0
            cur_max = 0
            for j in range(i, max(-1, i - k), -1):
                if cur_max < arr[j]:
                    cur_max = arr[j]
                val = dp[j] + cur_max * (i - j + 1)
                if cur_sum < val:
                    cur_sum = val
            dp[i + 1] = cur_sum
        return dp[-1]
