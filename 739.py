# url: https://leetcode.com/problems/daily-temperatures/


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t = temperatures
        stack = []
        ans = [0] * len(t)
        for i, e in enumerate(t):
            while stack and stack[-1][0] < e:
                old_temp, old_index = stack.pop()
                ans[old_index] = i - old_index
            stack.append((e, i))
        return ans
