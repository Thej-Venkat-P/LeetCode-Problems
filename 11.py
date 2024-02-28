# url: https://leetcode.com/problems/container-with-most-water/


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            if height[left] > height[right] :
                curr_area = height[right] * (right - left)
                if curr_area > max_area:
                    max_area = curr_area
                right -= 1
            else:
                curr_area = height[left] * (right - left)
                if curr_area > max_area:
                    max_area = curr_area
                left += 1
        return max_area