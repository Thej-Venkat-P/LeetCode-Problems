# url: www.leetcode.com/problems/longest-palindromic-substring/

# O(n^2) solution
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = [0, 1]

        def expand(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return (i + 1, j)

        for i in range(n - 1):
            a1, b1 = expand(i, i)
            a2, b2 = expand(i, i + 1)
            d1 = b1 - a1
            d2 = b2 - a2
            if d1 > d2 and d1 > ans[1] - ans[0]:
                ans = [a1, b1]
            elif d2 > ans[1] - ans[0]:
                ans = [a2, b2]

        return s[ans[0] : ans[1]]
"""


# O(n) solution - Manacher's algorithm
class Solution:
    def longestPalindrome(self, s: str) -> str:
        s = "#" + "#".join(s) + "#"
        n = len(s)

        c = 0
        r = 0
        p = [0] * n
        ans = [0, 1]

        for i in range(n):
            if i < r:
                p[i] = min(p[2 * c - i], r - i)
            else:
                p[i] = 0

            while (
                i + p[i] + 1 < n
                and i - p[i] - 1 >= 0
                and s[i + p[i] + 1] == s[i - p[i] - 1]
            ):
                p[i] += 1

            if i + p[i] > r:
                r = i + p[i]
                c = i

            if 2 * p[i] + 1 > ans[1] - ans[0]:
                ans = [i - p[i], i + p[i] + 1]

        return s[ans[0] : ans[1]].replace("#", "")
