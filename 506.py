# url: https://leetcode.com/problems/relative-ranks/


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score = enumerate(score)
        score = [(e, i) for i, e in score]
        score.sort(reverse=True)
        ans = [0]*len(score)
        for j, (_, i) in enumerate(score):
            if j > 2:
                ans[i] = str(j+1)
            elif j == 0:
                ans[i] = "Gold Medal"
            elif j == 1:
                ans[i] = "Silver Medal"
            else:
                ans[i] = "Bronze Medal"
        return ans