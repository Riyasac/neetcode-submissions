import re
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for word in strs:
            encoded_str += f"{len(word)}#{word}"
        return encoded_str

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        
        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])

            start = j + 1
            end = start + length
            result.append(s[start:end])
            i = end

        return result
