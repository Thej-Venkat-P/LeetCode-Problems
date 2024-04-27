class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [0 for i in range(n)]
        self.n = n

    def find_parent(self, x):
        if self.parent[x] == x:
            return x
        p = self.find_parent(self.parent[x])
        self.parent[x] = p
        return p

    def join(self, a, b):
        pa = self.find_parent(a)
        pb = self.find_parent(b)
        if pa == pb:
            return
        if self.size[pa] > self.size[pb]:
            self.size[pa] += self.size[pb]
            self.parent[pb] = pa
        else:
            self.size[pb] += self.size[pa]
            self.parent[pa] = pb


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        grid = [[0 if j == "0" else 1 for j in i] for i in grid]
        m = len(grid)
        n = len(grid[0])
        uf = UnionFind(m*n)
        found = set()
        for i in range(m):
            for j in range(n):
                if not grid[i][j]:
                    continue
                val = i*n + j
                found.add(val)
                if i > 0 and grid[i-1][j]:
                    uf.join(val, val-n)
                if j > 0 and grid[i][j-1]:
                    uf.join(val, val-1)
        parents = set()
        for val in found:
            parents.add(uf.find_parent(val))
        return len(parents)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(i, j):
            if not (0 <= i < m and 0 <= j < n) or grid[i][j] == "0":
                return 
            grid[i][j] = "0"
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        return count