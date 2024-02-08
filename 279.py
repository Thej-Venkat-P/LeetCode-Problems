# url: https://leetcode.com/problems/perfect-squares/


class Solution:
    def numSquares(self, n: int, cache={}) -> int:
        if n in cache:
            return cache[n]
        min_count = n
        for i in range(1, int(math.sqrt(n)) + 1):
            min_count = min(min_count, 1 + self.numSquares(n - i * i))
        cache[n] = min_count
        return min_count
