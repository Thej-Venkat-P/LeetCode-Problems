# url: https://leetcode.com/problems/longest-repeating-character-replacement/


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        max_f = 0
        max_len = 0
        counts = {}
        for end, char in enumerate(s):
            counts[char] = counts.get(char, 0) + 1
            if max_f < counts[char] :
                max_f = counts[char]
            while end - start + 1 - max_f > k:
                counts[s[start]] -= 1
                start += 1
            if max_len < end - start + 1 :
                max_len = end - start + 1
        return max_len
