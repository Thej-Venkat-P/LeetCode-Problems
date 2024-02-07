# url: https://leetcode.com/problems/sort-characters-by-frequency/


class Solution:
    def frequencySort(self, s: str) -> str:
        counts = collections.Counter(s)
        order = dict()

        for ch in counts:
            count = counts[ch]
            if count not in order:
                order[count] = []
            order[count].append(ch)

        ans = ""
        for i in sorted(order.keys())[::-1]:
            for j in order[i]:
                ans += j * i

        return ans
