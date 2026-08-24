class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        validP = {
            ']' : '[',
            '}' : '{',
            ')' : '('
        }

        for i in s:
            if i in validP:
                if stack and stack[-1] == validP[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        
        return True if not stack else False
        