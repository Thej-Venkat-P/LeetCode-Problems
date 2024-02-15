# url: https://leetcode.com/problems/largest-perimeter-triangle/                    


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        sum_val = 0
        ans = -1
        
        for num in nums:
            if num < sum_val:
                ans = num + sum_val
            sum_val += num
            
        return ans

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:

        while 1:
            if not nums:
                return -1  
            maxx = max(nums)
            suma = sum(nums) - maxx
            if suma<=maxx: 
                nums.remove(maxx)
            else: 
                break          
                
        return sum(nums)
                