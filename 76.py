# url: https://leetcode.com/problems/minimum-window-substring/


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        counts = collections.defaultdict(int)
        for char in t:
            counts[char] += 1

        start = 0
        st = set(t)
        ans = (-1, len(s))
        needed = len(t)

        for end, char in enumerate(s):
            if counts[(char)] > 0:
                needed -= 1
            counts[(char)] -= 1

            if needed == 0:
                while s[start] not in st or counts[s[start]] < 0:
                    counts[s[start]] += 1
                    start += 1
                    
                if end - start + 1 < ans[1] - ans[0]:
                    ans = (start, end + 1)
                counts[s[start]] += 1
                start += 1
                needed += 1

        return "" if ans[0] == -1 else s[ans[0]:ans[1]]
