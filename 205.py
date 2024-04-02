# url: https://leetcode.com/problems/isomorphic-strings/


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def check(s, t):
            mapping = {}
            for i in range(len(s)):
                if s[i] not in mapping:
                    mapping[s[i]] = t[i]
                elif t[i] != mapping[s[i]]:
                    return False
            return True
        return check(s, t) and check (t, s)

    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))

    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        for i in range(len(s)):
            if s[i] not in mapping:
                mapping[s[i]] = t[i]
            elif t[i] != mapping[s[i]]:
                return False
        vals = mapping.values()
        return len(vals) == len(set(vals))