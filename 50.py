# url: https://leetcode.com/problems/powx-n/


class Solution:
    def myPow(self, x: float, n: int) -> float:
        nn = n
        if n < 0:
            n = -n
            negative = True
        power = 1
        while n:
            if n & 1 != 0 :
                power *= x
            x *= x
            n = int(n//2)
        if nn < 0:
            power = 1/power
        return power