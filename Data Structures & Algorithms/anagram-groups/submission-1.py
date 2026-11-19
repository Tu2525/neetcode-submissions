class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answerdic = defaultdict(list)
        for i in strs:
            count = [0] * 26
            for y in i:
                count[ord(y) - ord("a")] += 1
            answerdic[tuple(count)].append(i)
        return answerdic.values()