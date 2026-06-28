class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        # Changed 'str' to 's'
        while i < len(s):
            j = i
            # Changed 'str' to 's'
            while s[j] != "#":
                j += 1
            
            # Changed 'Int' to 'int', and 'str' to 's'
            length = int(s[i:j])
            
            # Extract the actual string using the length
            res.append(s[j + 1 : j + 1 + length])
            
            # Move the pointer past the extracted string to the start of the next length
            i = j + 1 + length
            
        return res