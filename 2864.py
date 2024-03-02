# url: https://leetcode.com/problems/maximum-odd-binary-number/


class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        c1 = s.count("1")
        return "1"*(c1-1) + "0"*(len(s)-c1) + "1"