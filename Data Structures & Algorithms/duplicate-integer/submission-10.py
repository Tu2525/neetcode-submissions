class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ansDict = {}
        for num in nums:
            if num in ansDict:
                return True
            else:
                ansDict[num] = 1
        return False