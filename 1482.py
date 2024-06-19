# url: https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if n < m * k:
            return -1
        
        def check(mid):
            ans = 0
            curr_k = 0
            for num in bloomDay:
                if num <= mid:
                    curr_k += 1
                    if curr_k == k:
                        ans += 1
                        curr_k = 0
                else:
                    curr_k = 0
            return ans >= m

        left = min(bloomDay)
        right = max(bloomDay)
        ans = right
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
                ans = mid
            else:
                left = mid + 1
        
        return ans