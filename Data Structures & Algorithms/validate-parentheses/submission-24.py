class Solution:
    def isValid(self, s: str) -> bool:
        map = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        stack = []

        for val in s:
            if val in map:
                if stack and stack[-1] == map[val]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(val)
        return not stack