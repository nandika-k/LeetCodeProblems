class Solution:

    def encode(self, strs) -> str:
        string = ""
        for word in strs:
            string += str(len(word)) + "#" + word
        
        return string

    def decode(self, s: str):
        decoded = []
        pos = 0
        
        while pos < len(s):
            length = 0

            while s[pos] != "#":
                length = length*10 + int(s[pos])
                pos += 1
            
            decoded.append(s[pos+1:pos+length+1])
            pos += length + 1

        return decoded

sol = Solution()
print(sol.decode(sol.encode(["neet", "code"])))