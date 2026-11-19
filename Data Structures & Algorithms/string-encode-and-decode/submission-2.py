class Solution:

    def encode(self, strs: List[str]) -> str:
        longStr = ""
        for s in strs:
            longStr += s + "|"
        return longStr

    def decode(self, s: str) -> List[str]:
        ans = s.split("|")
        return ans[0:len(ans)-1]
