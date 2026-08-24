class Solution:
    def calPoints(self, operations: List[str]) -> int:
        total = 0
        stack = []
        for i in operations:
            if i == "+":
                newValue = stack[-1] + stack[-2]
                stack.append(newValue)
            elif i == "D":
                newValue = 2 * stack[-1]
                stack.append(newValue)
            elif i == "C":
                stack.pop()
            else:
                stack.append(int(i))
        
        return sum(stack)
