#New version
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0 
        j = len(s) - 1

        while i < j:
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue
            
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True

#Old version
import re

class Solution (object):
    def isPalindrome(self, s):
        s = (re.sub(r'[^\w]', '', s)).replace('_', '').lower()

        return s == s[::-1]

sol = Solution()
print(sol.isPalindrome("race a car"));
print(sol.isPalindrome("A man, a plan, a canal: Panama"))