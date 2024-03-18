# url: https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        merges = (-float('inf'), -float('inf'))
        points.sort()
        arrows = 0
        for a, b in points:
            if a > merges[1]:
                arrows += 1
                merges = (a, b)
            else:
                merges = (a, min(merges[1], b))
        return arrows
            

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        arrows = 0
        end = -float('inf')
        for a, b in points:
            if a > end:
                end = b
                arrows += 1
        return arrows