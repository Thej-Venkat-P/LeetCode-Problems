class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        sub = []

        def subset(index=0):
            if index == n:
                res.append(sub.copy())
                return
            subset(index + 1)
            sub.append(nums[index])
            subset(index + 1)
            sub.pop()
            
        subset()
        return res