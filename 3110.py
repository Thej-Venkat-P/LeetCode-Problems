# url: https://leetcode.com/problems/score-of-a-string/


class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        prev = ord(s[0])
        for c in s[1:]:
            curr = ord(c)
            score += abs(curr - prev)
            prev = curr
            
        return score