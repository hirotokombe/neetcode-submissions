class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
                continue

            if s and not stack:
                return False

            if char == ")" and stack[-1] != "(":
                return False
            elif char == "}" and stack[-1] != "{":
                return False
            elif char == "]" and stack[-1] != "[":
                return False
            else: 
                stack.pop()

    
                
        return not stack
            
        