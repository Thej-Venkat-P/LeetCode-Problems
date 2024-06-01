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
    

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_sum = 0
        for num in nums:
            xor_sum ^= num
        
        tmp = xor_sum
        first_change = 0
        while tmp & 1 == 0:
            tmp = tmp >> 1
            first_change += 1
        
        p = 1 << first_change
        num1 = num2 = 0
        for num in nums:
            if num & p:
                num1 ^= num
            else:
                num2 ^= num
        return [num1, num2]
            