# url : https://leetcode.com/problems/zigzag-conversion/


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = [""] * numRows
        k = 0
        direction = 1 if numRows != 1 else 0
        for i in s:
            res[k] += i
            k += direction
            if k == 0 or k == numRows - 1:
                direction *= -1

        return "".join(res)
