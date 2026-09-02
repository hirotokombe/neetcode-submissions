class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        calc_dict = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)
        }

        stack = []

        for token in tokens:
            if token in calc_dict:
                operand2 = stack.pop()
                operand1 = stack.pop()

                result = calc_dict[token](operand1, operand2)
                stack.append(result)
            else:
                stack.append(int(token))

        return stack[-1]