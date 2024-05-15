# url: https://leetcode.com/problems/find-the-safest-path-in-a-grid/


from heapq import heappush, heappop
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return 0

        def valid(i, j):
            return 0 <= i < n and 0 <= j < n
        neighbours = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        safety = [[-1]*n for _ in range(n)]
        safety_factor = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    safety_factor.append((0, i, j))a
                    safety[i][j] = 0

        while safety_factor:
            dist, i, j = safety_factor.popleft()
            # dist = safety[i][j] + 1
            
            for ni, nj in neighbours:
                ni += i
                nj += j
                if valid(ni, nj) and safety[ni][nj] == -1:
                    safety[ni][nj] = dist + 1
                    safety_factor.append((dist+1, ni, nj))

        # for i in grid:
        #     print(i)
        # for i in safety:
        #     print(i)
        
        max_heap = [( -safety[-1][-1], n-1, n-1)]
        found = set((n-1, n-1))

        while max_heap:
            s, i, j = heappop(max_heap)
            s *= -1
            if i == j == 0:
                return s

            for ni, nj in neighbours:
                ni += i
                nj += j
                if valid(ni, nj) and (ni, nj) not in found:
                    min_dist = min(s, safety[ni][nj])
                    found.add((ni, nj))
                    heappush(max_heap, (-min_dist, ni, nj))
        
        return -1