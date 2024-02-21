# url: https://leetcode.com/problems/generate-parentheses/


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        m = 2*n
        ans = []
        s = []
        def gen(open, close):
            if open == close == n:
                ans.append("".join(s))
                return
            if open < n:
                s.append("(")
                gen(open + 1, close)
                s.pop()
            if close < open:
                s.append(")")
                gen(open, close + 1)
                s.pop()
        gen(0, 0)
        return ans
