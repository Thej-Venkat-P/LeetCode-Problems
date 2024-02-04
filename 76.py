# url: https://leetcode.com/problems/minimum-window-substring/


class Solution:

    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t):
            return ""

        counts = collections.Counter(t)
        counts_t = collections.defaultdict(int)
        for i in counts:
            counts_t[i] = counts[i]

        start = 0
        need_count = len(t)
        ans = (0, len(s))

        for i, char in enumerate(s):
            if counts_t[char] > 0:
                need_count -= 1
            counts_t[char] -= 1
            if need_count == 0:
                while s[start] not in counts_t or counts_t[s[start]] < 0:
                    if s[start] in counts_t:
                        counts_t[s[start]] += 1
                    start += 1
                if i - start < ans[1] - ans[0]:
                    ans = (start, i)
                counts_t[s[start]] += 1
                need_count += 1
                start += 1

        return "" if ans[1] == len(s) else s[ans[0] : ans[1] + 1]
