class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ansDict = {}
        for num in nums:
            if num in ansDict:
                ansDict[num] += 1
            else:
                ansDict[num] = 1
        ans = []
        i = 0
        for key, value in sorted(ansDict.items(), key=lambda item: item[1], reverse=True):
            if i < k:
                ans.append(key)
                i += 1
            else:
                break
        return ans
            