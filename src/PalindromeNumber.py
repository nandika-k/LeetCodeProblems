class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
            
        original = str(x)
        reverse = str(x)[::-1]

        return original == reverse