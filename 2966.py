# url: https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(0, len(nums), 3):
            sub = nums[i : i + 3]
            if sub[2] - sub[0] > k:
                return []
            ans.append(sub)
        return ans
