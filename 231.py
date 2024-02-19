class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        x = 1
        while x < n:
            x = x * 2
        return x == n

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n!=0 and n & (n-1) == 0
    
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and bin(n).count('1') == 1

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & -n) == n

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and pow(2,31) % n == 0