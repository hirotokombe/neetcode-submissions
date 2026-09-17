class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        map = {
            "+" : lambda a, b : a + b,
            "-" : lambda a, b : a - b,
            "*" : lambda a, b : a * b,
            "/" : lambda a, b : int(a / b)
        }

        stack = []

        for token in tokens:
            if token in map:
                val2 = stack.pop()
                val1 = stack.pop()
                result = map[token](val1, val2)
                stack.append(result)
            else:
                stack.append(int(token))
        
        return stack[-1]
        