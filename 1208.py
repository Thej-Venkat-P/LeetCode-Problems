# url: https://leetcode.com/problems/get-equal-substrings-within-budget/


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        arr = []
        ans = 0
        for i in range(n):
            arr.append(abs(ord(s[i]) - ord(t[i])))

        left = 0
        curr_changes = 0
        for right in range(n):
            curr_changes += arr[right]
            while curr_changes > maxCost and left <= right:
                curr_changes -= arr[left]
                left += 1
            if ans < (val := right - left + 1):
                ans = val
        
        return ans