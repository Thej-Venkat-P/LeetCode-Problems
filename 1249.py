# url: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stack = []

        for i, char in enumerate(s) :
            if char == ")":
                if not stack:
                    s[i] = ""
                    continue
                stack.pop()
            elif char == "(" :
                stack.append(i)
        
        for idx in stack :
            s[idx] = ""
        
        return "".join(s)