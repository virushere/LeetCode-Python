class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for item in tokens:
            if item in ["+", "-", "/", "*"]:
                a = stack.pop()
                b = stack.pop()

                if item == "+":
                    stack.append(a+b)
                elif item == "-":
                    stack.append(b-a)
                elif item == "*":
                    stack.append(a*b)
                elif item == "/":
                    stack.append(int(b/a))
            else:
                stack.append(int(item))
        return stack[0]