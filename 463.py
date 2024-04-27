# url: https://leetcode.com/problems/island-perimeter/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 1:
                    continue
                curr = 4
                if i > 0 and grid[i-1][j] == 1:
                    curr -= 1
                if i < m-1 and grid[i+1][j] == 1:
                    curr -= 1
                if j > 0 and grid[i][j-1] == 1:
                    curr -= 1
                if j < n-1 and grid[i][j+1] == 1:
                    curr -= 1
                ans += curr
        return ans

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 1:
                    continue
                curr = 4
                if i > 0 and grid[i-1][j] == 1:
                    curr -= 2
                if j > 0 and grid[i][j-1] == 1:
                    curr -= 2
                ans += curr
        return ans

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    if not j or not grid[i][j - 1]:
                        perimeter += 2
                    if not i or not grid[i - 1][j]:
                        perimeter += 2
        return perimeter