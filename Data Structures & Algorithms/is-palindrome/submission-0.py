class Solution:
    def isPalindrome(self, s: str) -> bool:
        validString = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        l, r  = 0, len(validString) - 1
        while l <= r:
            if validString[l] != validString[r]:
                return False   
            l += 1
            r -= 1
        
        return True