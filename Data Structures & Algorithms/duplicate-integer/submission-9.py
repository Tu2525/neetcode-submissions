class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        answerDict = {}
        for item in nums:
            if item in answerDict:
                return True
            else:
                answerDict[item] = 1
        return False