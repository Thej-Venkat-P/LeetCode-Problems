# url: https://leetcode.com/problems/bag-of-tokens/


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        tokens = collections.deque(sorted(tokens))

        while tokens:
            while tokens and tokens[0] <= power:
                power -= tokens[0]
                tokens.popleft()
                score += 1
            if len(tokens) > 2 and score != 0:
                score -= 1
                power += tokens.pop()
            else:
                return score
        return score