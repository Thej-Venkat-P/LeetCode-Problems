# url: https://leetcode.com/problems/trapping-rain-water/


class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        left = 0
        right = len(height) - 1
        pl = height[0]
        pr = height[-1]
        while left < right:
            if pl < pr:
                while left < right and height[left] <= pl:
                    total += pl - height[left]
                    left += 1
            else:
                while right > left and height[right] <= pr:
                    total += pr - height[right]
                    right -= 1
            pl = height[left]
            pr = height[right]
        return total
    