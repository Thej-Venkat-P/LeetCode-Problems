# url: https://leetcode.com/problems/score-after-flipping-matrix


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        def flip(l):
            for i in range(len(l)):
                if l[i] == 0:
                    l[i] = 1
                else:
                    l[i] = 0
        
        for i in range(ROWS):
            if grid[i][0] == 0:
                flip(grid[i])
        
        counts = [ROWS]
        # print(grid)
        for j in range(1, COLS):
            c = 0
            for i in range(ROWS):
                if grid[i][j] == 1:
                    c += 1
            counts.append(max(c, ROWS - c))
        # print(counts)

        p = COLS - 1
        score = 0
        for count in counts:
            score += pow(2, p) * count
            p -= 1
        return score