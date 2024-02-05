class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = set()
        idx = {}
        for i,c in enumerate(s):
            if c in seen and c in idx:
                del idx[c]
            elif c not in seen:
                seen.add(c)
                idx[c] = i
        if not idx:
            return -1
        return idx[min(idx, key = lambda x: idx[x])]