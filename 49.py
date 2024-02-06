# url: https://leetcode.com/problems/group-anagrams/


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        for i, string in enumerate(strs):
            ss = "".join(sorted(string))
            d[ss].append(string)
        return list(d.values())
