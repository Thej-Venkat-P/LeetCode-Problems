# url: https://leetcode.com/problems/n-th-tribonacci-number/


class Solution:
    def tribonacci(self, n: int) -> int:
        a, b, c = 0, 1, 1
        if n < 3:
            if n:
                return 1
            return 0
        for i in range(3, n+1):
            n = a + b + c
            a, b, c = b, c, n
        return c
    