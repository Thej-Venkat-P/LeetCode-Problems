# url: https://leetcode.com/problems/longest-palindrome/


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        single = False
        ans = 0
        for key in counts:
            if counts[key] & 1 == 1:
                single = True
                ans += counts[key] - 1
            else:
                ans += counts[key]
        return ans + single