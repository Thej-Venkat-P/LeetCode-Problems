# url: https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/


class Solution:
    def minimumLength(self, s: str) -> int:
        start = 0
        end = len(s) - 1
        
        while start < end and s[start] == s[end]:
            start_char = s[start]
            start += 1
            end -= 1
            while start <= end and s[start] == start_char:
                start += 1
            while start <= end and s[end] == start_char:
                end -= 1

        return end - start + 1