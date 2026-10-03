class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator = {
            "+" : lambda a, b : a + b,
            "-" : lambda a, b : a - b,
            "*" : lambda a, b : a * b,
            "/" : lambda a, b : int(a / b)

        }

        stack = []

        for token in tokens:
            if token in operator:
                operand2 = stack.pop()
                operand1 = stack.pop()

                value = operator[token](operand1, operand2)
                stack.append(value)
            else:
                stack.append(int(token))
        
        return stack[-1]
