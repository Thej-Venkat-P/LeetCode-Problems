# url: https://leetcode.com/problems/find-all-groups-of-farmland/

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m = len(land)
        n = len(land[0])
        def expand(i, j):
            while i < m and land[i][j] == 1:
                i += 1
            i -= 1
            while j < n and land[i][j] == 1:
                j += 1
            j -= 1
            return (i, j)
        farms = []
        for i in range(m):
            for j in range(n):
                if not land[i][j] or (i > 0 and land[i-1][j]) or (j > 0 and land[i][j-1]):
                    continue
                ni, nj = expand(i, j)
                farms.append([i, j, ni, nj])
        return farms