class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0
        
        sign = 1

        if not s[0].isdigit():
            if s[0] == '-':
                sign = -1
                s = s[1:]
            elif s[0] == '+':
                s = s[1:]
            else:
                return 0

        index = 0
        for c in s:
            if c.isdigit():
                index += 1
            else:
                break
        
        if index == 0:
            return 0

        num = sign * int(s[:index])

        if sign == 1:
            return min(2**31 - 1, num)
        return max(-2**31, num)
        
    
sol = Solution()
print(sol.myAtoi("   -042"))
print(sol.myAtoi("0-1"))