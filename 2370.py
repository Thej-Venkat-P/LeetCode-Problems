# url: https://leetcode.com/problems/longest-ideal-subsequence/

class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        char_val = {chr(97 + i):i for i in range(26)}
        max_lengths = [0]*26
        for char in s:
            cv = char_val[char]
            min_lim = max(0, cv-k)
            max_lim = min(25, cv+k)
            max_neighbour_len = max(max_lengths[min_lim: max_lim+1])
            max_lengths[cv] = max_neighbour_len + 1
        return max(max_lengths)
