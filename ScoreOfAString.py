class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for i in range(len(s)-1):
            one = ord(s[i])
            two = ord(s[i+1])
            score += abs(one - two)
        return score

#still O(N) but better runtime
class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        lst = [ord(c) for c in s]
        for i in range(len(lst) - 1):
            score += abs(lst[i] - lst[i+1])
        return score