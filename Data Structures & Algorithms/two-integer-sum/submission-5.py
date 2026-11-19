class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ansDict = {}
        # i = 0
        # for num in nums:
        #     if ansDict[]
        #     ansDict[num] = i
        #     i += 1
        # print(ansDict)
        # for num in ansDict:
        #     needed = target - num
        #     if needed in ansDict:
        #         return [ansDict[num], ansDict[needed]]
        for i, n in enumerate(nums):
            diff = target - n
            if diff in ansDict:
                return [ansDict[diff],i]
            else:
                ansDict[n] = i


         