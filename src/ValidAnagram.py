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