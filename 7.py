# url: https://leetcode.com/problems/reverse-integer/


class Solution:
    def reverse(self, x: int) -> int:
        val = int(str(abs(x))[::-1]) * (1 if x >= 0 else -1)
        return val if (-(1 << 31) <= val < (1 << 31)) else 0


class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        rev = 0
        x = abs(x)
        while x:
            digit = x % 10
            if rev > (pow(2, 31) - digit) // 10:
                return 0
            rev = rev * 10 + digit
            x = x // 10
        return rev * sign
