class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # ansDict = {}
        # for i, n in enumerate(strs):
        #     value = 0
        #     for letter in n:
        #         value += ord(letter)
        #     ansDict[i] = value
        # finalDict = {}
        # for index, ascii_sum in ansDict.items():
        #     if ascii_sum not in finalDict:
        #         finalDict[ascii_sum] = []
        #     finalDict[ascii_sum].append(strs[index])
        # return list(finalDict.values())


        ansDict = defaultdict(list)
        for i in strs:
            count = [0] * 26 
            for j in i:
                index = ord(j) - ord('a')
                count[index] += 1
            ansDict[tuple(count)].append(i)
        return list(ansDict.values())