# number-of-submatrices-that-sum-to-target
# url: https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/


class Solution:
    def numSubmatrixSumTarget(self, matrix, target):
        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            for j in range(1, n):
                matrix[i][j] += matrix[i][j - 1]
        count = 0
        for c1 in range(n):
            for c2 in range(c1, n):
                sum_prefix = {0: 1}
                sum_val = 0
                for r in range(m):
                    sum_val += matrix[r][c2] - (matrix[r][c1 - 1] if c1 > 0 else 0)
                    count += sum_prefix.get(sum_val - target, 0)
                    sum_prefix[sum_val] = sum_prefix.get(sum_val, 0) + 1

        return count
