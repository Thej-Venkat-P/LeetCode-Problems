# url: https://www.leetcode.com/problems/intersection-of-two-arrays/


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        res = []
        for num in nums2:
            if num in nums1:
                res.append(num)
                nums1.remove(num)
        return res

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1).intersection(set(nums2))