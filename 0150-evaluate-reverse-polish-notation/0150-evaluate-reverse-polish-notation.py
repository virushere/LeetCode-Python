class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack, ops = [], ['+','-','*','/']

        for c in tokens:
            if c not in ops:
                stack.append(int(c))
            else:
                a, b = stack.pop(), stack.pop()
                if c=='+':
                    stack.append(a+b)
                elif c=='-':
                    stack.append(b-a)
                elif c=='*':
                    stack.append(a*b)
                elif c=='/':
                    stack.append(int(b/a))
        return stack[0]