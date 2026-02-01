class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = current_num = 0
        sign = 1
        for i in s:
            if i == '+':
                result = result + sign * current_num
                sign = 1
                current_num = 0 
            elif i == '-':
                result = result + sign * current_num
                sign = -1
                current_num = 0 
            elif i == '(':
                stack.append((result,sign))
                sign = 1
                result = current_num = 0 
            elif i == ')':
                result = result + sign * current_num
                prev_result, prev_sign = stack.pop()
                current_num = 0
                sign = 1
                result = prev_result + prev_sign * result
            elif i == ' ':
                continue
            else:
                if i.isdigit():
                    current_num = current_num * 10 + int(i)
        result = result + sign * current_num
        return result