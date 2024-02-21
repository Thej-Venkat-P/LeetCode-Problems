# url: https://leetcode.com/problems/bitwise-and-of-numbers-range/


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        diff = right - left
        if diff == 0:
            return left
        ans = 0
        left_bin = bin(left)[2:][::-1]
        right_bin = bin(right)[2:][::-1]
        digits = len(left_bin)
        for power in reversed(range(digits)):
            if pow(2, power) <= diff:
                break
            if left_bin[power] == "0" or right_bin[power] == "0":
                continue
            ans += pow(2, power)

        return ans


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        lb = bin(left)[2:]
        rb = bin(right)[2:]
        n = len(rb)
        if n > len(lb):
            return 0

        i = 0
        while i < n:
            if lb[i] != rb[i]:
                break
            i += 1

        return int(rb[:i] + "0" * (n - i), 2)
