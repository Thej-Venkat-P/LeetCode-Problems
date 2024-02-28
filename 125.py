# url: https://leetcode.com/problems/valid-palindrome/


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub("[^a-zA-Z0-9]","",s).lower()
        return hash(s) == hash(s[::-1])
        return s == s[::-1]