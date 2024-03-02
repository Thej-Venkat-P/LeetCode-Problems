# url: https://leetcode.com/problems/sliding-window-maximum/


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
        ans = [nums[q[0]]]

        for ni in range(k, len(nums)):
            if q[0] == ni - k:
                q.popleft()
            nv = nums[ni]
            while q and nv >= nums[q[-1]]:
                q.pop()
            q.append(ni)
            ans.append(nums[q[0]])
            
        return ans