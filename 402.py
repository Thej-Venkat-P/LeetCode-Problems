# url: https://leetcode.com/problems/remove-k-digits/


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        if n <= k:
            return '0'
        stack = []
        for char in num:
            while stack and char < stack[-1] and k:
                stack.pop()
                k -= 1
            stack.append(char)
        for i in range(k):
            stack.pop()
        ans = "".join(stack[:]).lstrip('0')
        return ans if ans else '0'