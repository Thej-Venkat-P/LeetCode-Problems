# url: https://leetcode.com/problems/largest-divisible-subset/


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans_list = {-1 : set()}

        for num in nums:
            ans_list[num] = max([ans_list[k] for k in ans_list if num%k==0], key = len) | {num} #Union

        return max(ans_list.values(), key = len)