# url: https://leetcode.com/problems/sum-of-square-numbers


import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        mid = c // 2
        for i in range(int(math.sqrt(mid)) + 1):
            first = i**2
            second = c - first
            ssqrt = math.sqrt(second)
            if int(ssqrt) == ssqrt:
                return True
        return False

# A mathematical theorem by Fermat states that a number can be represented as 
# the sum of two squares if and only if all prime factors of the form ( 4k + 3 ) 
# have even powers in its prime factorization.

class Solution(object):
    def judgeSquareSum(self, c):
        divisor = 2
        while divisor * divisor <= c:
            if c % divisor == 0:
                exponentCount = 0
                while c % divisor == 0:
                    exponentCount += 1
                    c //= divisor
                if divisor % 4 == 3 and exponentCount % 2 != 0:
                    return False
            divisor += 1
        return c % 4 != 3
    

# Two pointer Solution
class Solution(object):
    def judgeSquareSum(self, c):
        left = 0
        right = int(math.sqrt(c))
        while left <= right:
            s = left ** 2 + right ** 2
            if s == c:
                return True
            if s < c:
                left += 1
            else:
                right -= 1
        return False