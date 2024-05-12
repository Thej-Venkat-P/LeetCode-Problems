# url: https://leetcode.com/problems/minimum-cost-to-hire-k-workers/


from heapq import heappop, heappush

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(wage)
        wage_per_quality = [wage[i]/quality[i] for i in range(n)]
        comb = list(zip(quality, wage_per_quality))
        comb.sort(key=lambda x: x[1])
        res = float('inf')

        max_heap = []
        total_quantity = 0

        for q, rate in comb[:k]:
            heappush(max_heap, -q)
            total_quantity += q
        res = total_quantity * rate

        for q, rate in comb[k:]:
            heappush(max_heap, -q)
            total_quantity += q
            total_quantity += heappop(max_heap)
            if (new_min := total_quantity * rate) < res:
                res = new_min
        
        return res