# url: https://leetcode.com/problems/longest-valid-parentheses/


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans = 0
        stack = [-1]

        for i in range(len(s)):
            if s[i] == "(": 
                stack.append(i)
            else:
                if stack: 
                    stack.pop()
                if stack: 
                    ans = max(ans, i - stack[-1])
                else: 
                    stack.append(i)
        
        return ans