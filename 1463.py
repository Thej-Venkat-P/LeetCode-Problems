# url: https://leetcode.com/problems/cherry-pickup-ii/


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        COLS = len(grid[0])
        ROWS = len(grid)

        zeroes = dict()
        for c1 in range(COLS - 1):
            for c2 in range(c1+1, COLS):
                zeroes[(c1,c2)] = 0

        col_grid = zeroes.copy()
        pdc = list(product([-1,0,1], [-1,0,1]))

        for row_idx in range(ROWS-1, -1, -1):
            row = grid[row_idx]
            temp = zeroes.copy()
            for c1 in range(min(row_idx + 1, COLS-1)):
                for c2 in range(max(c1+1, COLS-row_idx-1), COLS):
                    res = 0
                    col_val = row[c1] + row[c2]
                    for c1d, c2d in pdc:
                        tc1 = c1+c1d
                        tc2 = c2+c2d
                        if 0 <= tc1 < tc2 < COLS:
                            val = col_grid[(tc1,tc2)] + col_val
                            if val > res:
                                res = val
                    temp[(c1,c2)] = res
            col_grid = temp
        
        return col_grid[(0,COLS-1)]
    