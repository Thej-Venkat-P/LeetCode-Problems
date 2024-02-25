# url: https://leetcode.com/problems/check-if-it-is-a-good-array/

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        nums = set(nums)
        if 1 in nums:
            return False
        if len(nums) == 1:
            return True

        nums = sorted(nums, reverse = True)
        n = len(nums)

        for i in range(n - 1):
            for j in range(i + 1, n):
                if math.gcd(nums[i], nums[j]) != 1:
                    nums[j] *= nums[i]
                    break
            else:
                return False
        return True
    
class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.sizes = [1] * n
        self.count = n
    
    def find_parent(self, m):
        if self.parents[m] != m:
            self.parents[m] = self.find_parent(self.parents[m])
        return self.parents[m]
    
    def join(self, a, b):
        pa, pb = self.find_parent(a), self.find_parent(b)
        if pa == pb:
            return 
        self.count -= 1
        if self.sizes[pa] > self.sizes[pb]:
            self.sizes[pa] += self.sizes[pb]
            self.parents[pb] = pa
        else:
            self.sizes[pb] += self.sizes[pa]
            self.parents[pa] = pb


class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        uf = UnionFind(len(nums))
        factor_index = {}
        for i,n in enumerate(nums):
            for p in range(2, int(math.sqrt(n)) + 1):
                if n % p == 0:
                    if p in factor_index:
                        uf.join(i, factor_index[p])
                    else:
                        factor_index[p] = i
                    while n % p == 0:
                        n = n // p
            if n > 1:
                if n in factor_index:
                    uf.join(i, factor_index[n])
                else:
                    factor_index[n] = i
        
        return uf.count == 1