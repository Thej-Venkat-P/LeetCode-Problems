# Link: https://leetcode.com/problems/insert-interval/


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []
        
        for i, interval in enumerate(intervals):
            if newInterval[0] > interval[1]:
                merged.append(interval)
                
            elif newInterval[1] < interval[0]:
                merged.append(newInterval)
                return merged + intervals[i:]
                
            else:
                newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]

        merged.append(newInterval)
        return merged