# url: https://leetcode.com/problems/ipo


from heapq import heappush, heappop
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        profits = [(capital[i], profits[i]) for i in range(n)]
        profits.sort()
        hq = []
        i = 0

        for _ in range(k):
            while i < n and profits[i][0] <= w:
                heappush(hq, -profits[i][1])
                i += 1
            if not hq:
                return w
            w += -heappop(hq)

        return w