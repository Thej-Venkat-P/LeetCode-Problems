# url: https://leetcode.com/problems/magnetic-force-between-two-balls/


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)
        def place(mid, m):
            m -= 1
            i = 1
            curr = position[0]
            while i < n and m:
                if position[i] - curr < mid:
                    i += 1
                    continue
                curr = position[i]
                m -= 1
            return m == 0
        
        lo = 1
        hi = (position[-1] - position[0]) // (m - 1) + 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if place(mid, m):
                lo = mid + 1
            else:
                hi = mid - 1
        return hi