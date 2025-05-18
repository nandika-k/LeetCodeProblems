'''
Given a string s, find the length of the longest substring without duplicate characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0 or len(s) == 1:
            return len(s)
        """
        :type s: str
        :rtype: int
        """
        start = 0
        end = 2
        max_length = 1

        while end <= len(s):
            character = s[end-1:end]
            substring = s[start:end-1]
            if character not in substring:
                end += 1
                max_length = max(max_length, end - start - 1)
            else:
                start += substring.index(character)+1
                end += 1

        return max_length

sol = Solution()
print(sol.lengthOfLongestSubstring("bbtablud")) # 6
