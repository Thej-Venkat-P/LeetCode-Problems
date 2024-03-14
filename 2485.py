# url: https://leetcode.com/problems/pivot-integer/


class Solution:
    def pivotInteger(self, n: int) -> int:
        ans = math.sqrt(n*(n+1)/2)
        return int(ans) if ans == int(ans) else -1