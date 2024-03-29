# url: https://leetcode.com/problems/count-number-of-nice-subarrays/


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)
        pleft = 0
        left = 0
        maxi = max(set(nums))

        for right in range(n):
            if nums[right] == maxi:
                k -= 1

            if k == 0 :
                pleft = left

                while k == 0:
                    if nums[left] == maxi:
                        k += 1
                    left += 1

                ans += (left - pleft) * (n - right)

        return ans

    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxi = nums[0]
        idx = [0]
        n = len(nums)
        for i, num in enumerate(nums[1:]):
            if num > maxi :
                maxi = num
                idx = [i+1]
            elif num == maxi:
                idx.append(i+1)
        idx = [-1] + idx
        ans = 0
        for i in range(k, len(idx)):
            left = i - k + 1
            right = i
            ans += (idx[left] - idx[left - 1]) * (n - idx[right])
        return ans