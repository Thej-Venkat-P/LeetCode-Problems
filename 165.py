# url: https://leetcode.com/problems/compare-version-numbers/


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split(".")
        version2 = version2.split(".")
        n1, n2 = len(version1), len(version2)
        mn = min(n1, n2)

        for i in range(mn):
            v1 = int(version1[i])
            v2 = int(version2[i])
            if v1 > v2:
                return 1
            elif v2 > v1:
                return -1

        if n1 > n2:
            version = version1
            v = 1
        else:
            version = version2
            v = 2
        
        for i in range(mn, len(version)):
            if version[i].strip("0"):
                return 1 if v == 1 else -1

        return 0