class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        strs.sort()
        first = strs[0]
        last = strs[-1]
        minLen = min(len(first), len(last))

        if minLen == 0:
            return ""

        for i in range(minLen):
            if first[i] != last[i]:
                return first[0:i]
        if len(first) < len(last):
            return first
        return last