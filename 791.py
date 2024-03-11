# url: https://leetcode.com/problems/custom-sort-string/


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counts = collections.Counter(s)
        t = ""
        for o in order:
            if o in counts:
                t += o * counts[o]
                del counts[o]
        for i in counts:
            t += i * counts[i]
        return t
