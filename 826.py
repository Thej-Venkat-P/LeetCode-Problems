# urls: https://leetcode.com/problems/most-profit-assigning-work/


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        worker.sort()
        n = len(jobs)
        total_profit = curr_max_profit = i = 0

        for w in worker:
            while i < n and jobs[i][0] <= w:
                if jobs[i][1] > curr_max_profit:
                    curr_max_profit = jobs[i][1]
                i += 1
            total_profit += curr_max_profit
        return total_profit