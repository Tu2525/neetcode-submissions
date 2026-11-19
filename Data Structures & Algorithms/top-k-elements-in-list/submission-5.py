class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # ansDict = {}
        # for num in nums:
        #     if num in ansDict:
        #         ansDict[num] += 1
        #     else:
        #         ansDict[num] = 1
        # ans = []
        # i = 0
        # for key, value in sorted(ansDict.items(), key=lambda item: item[1], reverse=True):
        #     if i < k:
        #         ans.append(key)
        #         i += 1
        #     else:
        #         break
        # return ans
        # Make a list and add a list of keys in each index.
        ansDict = {}
        freq = [[] for i in range(len(nums) + 1)]
        # print(f"this is freq {freq}")
        for num in nums:
            ansDict[num] = 1 + ansDict.get(num,0)
        # print(f"this is ansDict {ansDict}")
        for num, cnt in ansDict.items():
            freq[cnt].append(num)
        # print(f"this is freq again {freq}")
        ans = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans