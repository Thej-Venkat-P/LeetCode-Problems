# url: https://leetcode.com/problems/string-to-integer-atoi/


#
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()

        if not s:
            return 0

        sign = 1
        r = pow(2, 31) - 1
        if s[0] == "-":
            sign = -1
            r = r + 1
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]

        val = 0
        for i, c in enumerate(s):
            if not c.isdigit():
                break
            val = val * 10 + int(c)

        val = val if val < r else r
        return sign * val
