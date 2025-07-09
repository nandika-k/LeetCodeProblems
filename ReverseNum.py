#absolutely horrible runtime, but good memory-wise
class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
            x = -x
        result = 0

        while x != 0:
            result = result*10 + (x % 10)
            x = x//10

        if result > 2**31 - 1 or result < -2**31:
            return 0
        return sign*result
        
sol = Solution()
print(sol.reverse(123))
print(sol.reverse(-123))