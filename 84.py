# url: https://leetcode.com/problems/largest-rectangle-in-histogram/


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = []
        ans = 0
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] >= h:
                new_h = heights[stack.pop()]
                w = i - stack[-1] - 1 if stack else i
                ans = max(ans, new_h*w)
            stack.append(i)
        return ans


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [0]
        ans = 0
        for i, h in enumerate(heights):
            prev_h = heights[stack[-1]]
            if h > prev_h:
                stack.append(i)
            elif h == prev_h:
                pass
            else:
                while stack and heights[stack[-1]] > h:
                    last = stack.pop()
                    new_h = heights[last]
                    new_w = i - last
                    if new_h*new_w > ans:
                        ans = new_h*new_w
                stack.append(last)
                heights[last] = h
        return ans
