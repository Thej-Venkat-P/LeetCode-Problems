# url: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one


class Solution:
    def numSteps(self, s: str) -> int:
        s = list(map(int, s))
        carry = 0
        steps = 0

        for digit in s[:0:-1]:
            if digit and carry:
                steps += 1
            elif not digit and not carry:
                steps += 1
            else:
                carry = 1
                steps += 2
        
        if carry:
            steps += 1

        return steps

