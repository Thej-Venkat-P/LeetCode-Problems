# url: https://leetcode.com/problems/reverse-string/


class Solution:
    def reverseString(self, s: List[str]) -> None:
        n = len(s)
        i = 0
        j = n - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            j -= 1
            i += 1
        return s
        