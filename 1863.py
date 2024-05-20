class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        xor_sums = deque([0])
        for num in nums:
            n = len(xor_sums)
            for i in range(n):
                elem = xor_sums.popleft()
                xor_sums.append(elem^num)
                xor_sums.append(elem)
        return sum(xor_sums)

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        or_sum = 0
        for num in nums:
            or_sum = or_sum | num
        return or_sum * (1 << (len(nums) - 1))
    