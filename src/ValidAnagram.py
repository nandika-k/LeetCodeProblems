#More efficient version - O(26+N)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alphabet = [0]*26

        for a,b in zip(s,t):
            alphabet[ord(a) - ord('a')] += 1
            alphabet[ord(b) - ord('a')] -= 1

        for freq in alphabet:
            if freq != 0:
                return False
        return True

#Readable version - O(26N)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alphabet = "abcdefghijklmnopqrstuvqxyz"

        if len(s) != len(t):
            return False

        for letter in alphabet:
            if s.count(letter) != t.count(letter):
                return False
        return True