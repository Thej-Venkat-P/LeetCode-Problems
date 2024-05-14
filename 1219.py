class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        non_zero = True
        s = 0
        for i in range(m):
            for j in range(n):
                if not grid[i][j]:
                    non_zero = False
                    break
                s += grid[i][j]
        if non_zero:
            return s
        
        def isStartingPoint(i, j):
            directions = [(i+1, j), (i,j+1), (i-1,j), (i,j-1)]
            direction = 0
            for (row_idx, col_idx) in directions:
                if row_idx<m and col_idx<n and grid[row_idx][col_idx]!=0:
                    direction += 1
            return direction <= 2

        def dfs(i, j):
            if not 0 <= i < m or not 0 <= j < n or grid[i][j] == 0:
                return 0
            neighbours = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
            tmp = grid[i][j]
            res = 0
            grid[i][j] = 0
            for ni, nj in neighbours:
                if (nval := tmp + dfs(ni, nj)) > res:
                    res = nval
            grid[i][j] = tmp
            return res

        ans = 0
        for i in range(m):
            for j in range(n):
                if not grid[i][j]:
                    continue
                if isStartingPoint(i, j) and (ns := dfs(i, j)) > ans: 
                    ans = ns
        return ans