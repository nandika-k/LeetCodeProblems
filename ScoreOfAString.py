class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for i in range(len(s)-1):
            one = ord(s[i])
            two = ord(s[i+1])
            score += abs(one - two)
        return score