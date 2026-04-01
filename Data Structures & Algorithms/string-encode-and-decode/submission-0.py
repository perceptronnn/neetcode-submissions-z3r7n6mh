class Solution:

    def encode(self, strs: List[str]) -> str:
        encoding = ""
        for s in strs:
            encoding += str(len(s)) + "#" + s
        return encoding

    def decode(self, s: str) -> List[str]:
        decoding = []
        idx = 0
        print(s)
        while idx < (len(s)):
            print(idx)
            l = ""
            while s[idx] != "#":
                l += s[idx]
                idx += 1
            l = int(l)
            idx += 1
            word = ""
            while l != 0:
                word += s[idx]
                idx += 1
                l -= 1
            decoding.append(word)
        return decoding
