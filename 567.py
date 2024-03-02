# url: https://leetcode.com/problems/permutation-in-string/


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n2 < n1:
            return False

        c1 = [0]*26
        c2 = c1.copy()
        def idx(c):
            return ord(c) - ord("a")
        
        for i in range(n1):
            c1[idx(s1[i])] += 1
            c2[idx(s2[i])] += 1

        if c1 == c2:
            return True
        j = 0

        for i in range(n1, n2):
            c2[idx(s2[j])] -= 1
            c2[idx(s2[i])] += 1
            if c1 == c2:
                return True
            j += 1
        return False
