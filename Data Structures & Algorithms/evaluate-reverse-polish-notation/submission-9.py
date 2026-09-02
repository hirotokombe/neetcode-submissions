class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        total = 0
        calc_dict = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)
        }
        stack = []
        i = 0
        while i < len(tokens):
            while i < len(tokens) and tokens[i] not in calc_dict:
                stack.append(int(tokens[i]))
                i += 1

            if i < len(tokens) and tokens[i] in calc_dict:
                operand2 = stack.pop()
                operand1 = stack.pop()

                total = calc_dict[tokens[i]](operand1, operand2)
                stack.append(total)

            i += 1

        return stack[-1]
        
   