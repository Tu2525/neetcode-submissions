class Solution:
    # def encode(self, strs: List[str]) -> str:
    #     longStr = ""
    #     for s in strs:
    #         longStr += s + "|"
    #     return longStr

    # def decode(self, s: str) -> List[str]:
    #     ans = s.split("|")
    #     return ans[0:len(ans)-1]
    #Simple Elegant, but no, they want it more complicated!
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:   
        res, i = [], 0
        while i < len(s):
            j = i   
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1 : j+1+length])
            i = j + 1 + length
        return res
