# url: https://leetcode.com/problems/maximize-happiness-of-selected-children/


from heapq import heappush, heappop
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        # Using Heap
        kHappiness = []
        # O(NlogK)
        for h in happiness:
            heapq.heappush(kHappiness, h)
            if len(kHappiness) > k:
                heapq.heappop(kHappiness)
        
        answer = 0
        # O(KlogK)
        while k:
            happiness = heapq.heappop(kHappiness)
            answer += max(0, happiness - k + 1)
            k -= 1
        return answer