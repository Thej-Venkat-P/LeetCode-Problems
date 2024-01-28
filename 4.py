# url: https://leetcode.com/problems/median-of-two-sorted-arrays/


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        m, n = len(A), len(B)
        if m > n:
            A, B = B, A
            m, n = n, m
        total = m + n
        half = total // 2
        i, j = 0, m - 1

        while True:
            Am = (i + j) // 2
            Bm = half - Am - 2

            A_right = A[Am + 1] if Am < m - 1 else float("inf")
            A_left = A[Am] if Am >= 0 else -float("inf")
            B_right = B[Bm + 1] if Bm < n - 1 else float("inf")
            B_left = B[Bm] if Bm >= 0 else -float("inf")

            if A_right >= B_left and B_right >= A_left:
                if total % 2 == 0:
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2
                else:
                    return min(A_right, B_right)
            elif A_right < B_left:
                i = Am + 1
            else:
                j = Am - 1

        return None
