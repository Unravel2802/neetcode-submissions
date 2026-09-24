class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def operate(operation, a, b):
            match operation:
                case '+':
                    return a + b
                case '-':
                    return a - b
                case '*':
                    return a * b
                case '/':
                    return int(a / b)

        stack = []
        operations = ['+', '-', '*', '/']
        for token in tokens:
            if token in operations:
                num1 = int(stack[-2])
                num2 = int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(operate(token, num1, num2))
            else:
                stack.append(token)
        return int(stack[-1])
