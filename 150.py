# url: https://leetcode.com/problems/evaluate-reverse-polish-notation/


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                stack.append(-stack.pop() + stack.pop())
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                stack.append(int((1 / stack.pop()) * stack.pop()))
            else:
                stack.append(int(token))
        return stack[0]

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ("+", "-", "*", "/"):
                val2 = stack.pop()
                val1 = stack.pop()
                if token == "+":
                    stack.append(val1 + val2)
                elif token == "-":
                    stack.append(val1 - val2)
                elif token == "*":
                    stack.append(val1 * val2)
                elif token == "/":
                    stack.append(int(val1 / val2))
                print(stack[-1])
            else:
                stack.append(int(token))

        return stack[0]
            