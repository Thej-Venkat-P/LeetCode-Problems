# url: https://leetcode.com/problems/furthest-building-you-can-reach/

import heapq


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        jumps = []

        for i in range(n - 1):
            diff = heights[i + 1] - heights[i]
            if diff > 0:
                if len(jumps) < ladders:
                    heapq.heappush(jumps, diff)
                else:
                    bricks -= heapq.heappushpop(jumps, diff)
                if bricks < 0:
                    return i

        return n - 1
