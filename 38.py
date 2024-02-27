# url: https://leetcode.com/problems/valid-sudoku/


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def validate(l):
            s = set()
            for elem in l:
                if elem != ".":
                    if elem in s:
                        return False
                    s.add(elem)
            return True
        for l in board:
            if not validate(l):
                return False
        for l in zip(*board):
            if not validate(l):
                return False
        for i in (0,3,6):
            for j in (0,3,6):
                l = []
                for k in range(3):
                    l.extend(board[i + k][j:j+3])
                if not validate(l):
                    return False
        return True
    

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        positions = []
        for i in range(9):
            for j in range(9):
                elem = board[i][j]
                if elem != ".":
                    positions.extend([(i,-1,elem), (-1,j,elem), (i//3,j//3,elem)])
        return len(positions) == len(set(positions))