# url: https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = max_len = 0
        seen = {}
        for i, e in enumerate(s):
            if seen.get(e, -1) >= left:
                left = seen[e] + 1
            seen[e] = i
            max_len = max(max_len, i - left + 1)
        return max_len
