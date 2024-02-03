#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#


# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        m = 2 * numRows - 2
        if m == 0:
            return s
        n = len(s)
        res = ""
        for i in range(numRows):
            for j in range(i, n, m):
                res += s[j]
                if i != 0 and i != numRows - 1 and j + m - 2 * i < n:
                    res += s[j + m - 2 * i]
                print(res)
        return res


# @lc code=end
