# url: https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/


class Solution:
    def maxDepth(self, s: str) -> int:
        ans = c = 0
        for char in s:
            if char == "(" :
                c += 1
                if c > ans:
                    ans = c
            elif char == ")" :
                c -= 1
        return ans