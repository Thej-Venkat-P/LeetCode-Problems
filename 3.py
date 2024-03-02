# url: https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        found = {}
        start = 0
        max_len = 0
        for end, char in enumerate(s):
            if found.get(char, -1) >= start:
                start = found[char] + 1
            found[char] = end
            if end - start + 1 > max_len:
                max_len = end - start + 1
        return max_len
