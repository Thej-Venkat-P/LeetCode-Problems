# url: https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counts = collections.Counter(arr).values()
        ans = len(counts)
        counts = collections.Counter(counts)
        
        for i in sorted(counts.keys()):
            if k >= i * counts[i]:
                k -= i * counts[i]
                ans -= counts[i]
            else:
                ans -= k//i
                break

        return ans