# url: https://leetcode.com/problems/regular-expression-matching/


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p = re.sub(r"\*{2,}", "*", p)
        n = len(s)
        m = len(p)

        @functools.lru_cache(None)
        def search(i, j):
            if i == n and j == m:
                return True
            elif j == m:
                return False

            match = i < n and (s[i] == p[j] or p[j] == ".")
            if j + 1 < m and p[j + 1] == "*":
                if match:
                    return search(i + 1, j) or search(i, j + 2)
                return search(i, j + 2)
            elif match:
                return search(i + 1, j + 1)

        return search(0, 0)
