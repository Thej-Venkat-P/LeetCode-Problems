# url: https://leetcode.com/problems/palindromic-substrings/


class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0

        i = 0
        while i<n:
            j = i-1
            k = i
            while k<n-1 and s[k]==s[k+1]:
                k += 1
            m = k-j
            ans += (m * (m+1)) // 2
            i,k = k + 1, k + 1
            while j >= 0 and k < n and s[j] == s[k]:
                ans += 1
                j -= 1
                k += 1
        
        return ans