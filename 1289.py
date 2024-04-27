# url: https://leetcode.com/problems/minimum-falling-path-sum-ii/

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        prev = grid[0]
        n = len(grid)

        def find_mins(arr):
            first = second = (float('inf'), -1)
            for i, val in enumerate(arr):
                if val < first[0]:
                    second, first = first, (val, i)
                elif val < second[0]:
                    second = (val, i)
            return first, second

        first, second = find_mins(prev)
        for i in range(1, len(grid)):
            curr = grid[i]
            for i in range(first[1]):
                curr[i] += first[0]
            curr[first[1]] += second[0]
            for i in range(first[1] + 1, n):
                curr[i] += first[0]
            prev = curr
            first, second = find_mins(prev)

        return first[0]