class Solution:
    def dfs(self, nums: List[int], idx: int, k: int, mp: defaultdict) -> int:
        if idx == len(nums):
            return 1

        taken = 0
        if mp[nums[idx] - k] == 0 and mp[nums[idx] + k] == 0:
            mp[nums[idx]] += 1
            taken = self.dfs(nums, idx + 1, k, mp)
            mp[nums[idx]] -= 1
        
        notTaken = self.dfs(nums, idx + 1, k, mp)
        
        return taken + notTaken

    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        mp = defaultdict(int)
        ans = self.dfs(nums, 0, k, mp)
        return ans - 1

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        found = set()
        groups = []
        
        for num in count:
            if num in found:
                continue
            groups.append([])
            temp = num
            while temp in count:
                temp -= k
            temp += k
            while temp in count:
                found.add(temp)
                groups[-1].append(temp)
                temp += k

        @lru_cache(None)
        def find_bs(group, i):
            if i >= len(group):
                return 1
            curr = group[i]
            taken = ((2 ** count[curr]) - 1) * find_bs(group, i+2)
            not_taken = find_bs(group, i+1)
            return taken + not_taken

        res = 1
        for group in groups:
            bs = find_bs(tuple(group), 0)
            res *= bs

        return res - 1