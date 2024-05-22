# url: https://leetcode.com/problems/palindrome-partitioning/


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        cache = {}
        def check_pali(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        @lru_cache(None)
        def partition(i):
            if i == n:
                return [[]]
            
            res = []
            ans = []
            
            for j in range(i + 1, n + 1):
                if check_pali(s, i, j - 1):
                    first_part = [s[i:j]]
                    for second_part in partition(j):
                        ans = first_part + second_part
                        res.append(ans)
            
            return res

        return partition(0)