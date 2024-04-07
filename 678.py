# url: https://leetcode.com/problems/valid-parenthesis-string/


class Solution:
    def checkValidString(self, s: str) -> bool:
        open_stack = []
        random_stack = []

        for i, char in enumerate(s):
            if char == "(" :
                open_stack.append(i)
            elif char == "*" :
                random_stack.append(i)
            else :
                if open_stack :
                    open_stack.pop()
                    continue
                elif random_stack :
                    random_stack.pop()
                    continue
                else :
                    return False
        
        while open_stack and random_stack :
            if random_stack[-1] > open_stack[-1] :
                random_stack.pop()
                open_stack.pop()
            else:
                return False
        
        return open_stack == []


class Solution:
    def checkValidString(self, s: str) -> bool:
        left_min = left_max = 0
        # left_min is the index of the left most open bracket
        # left_max is the index of the right most open bracket
        
        for c in s :
            if c == "(" :
                left_min += 1
                left_max += 1
            elif c == ")" :
                left_min -= 1
                left_max -= 1
            else :
                left_min -= 1
                left_max += 1
            if left_max < 0 :
                return False
            if left_min < 0 :
                left_min = 0      
        
        return left_min == 0