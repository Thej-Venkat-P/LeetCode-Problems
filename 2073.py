# url: https://leetcode.com/problems/time-needed-to-buy-tickets


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        final = tickets[k]
        ans = 0
        for i in range(k+1):
            ans += min(tickets[i], final)
        final -= 1
        for i in range(k+1, len(tickets)):
            ans += min(tickets[i], final)
        return ans