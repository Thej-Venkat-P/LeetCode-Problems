# url: https://leetcode.com/problems/single-number-iii/


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        diff = functools.reduce(operator.xor, nums)

        diff &= -diff

        first = second = 0
        for num in nums :
            if num & diff == 0 :
                first ^= num
            else :
                second ^= num

        return [first, second]