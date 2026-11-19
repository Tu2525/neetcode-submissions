class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix = [1]
        # postfix = [1]
        # res = []
        # for num in nums:
        #     prefix.append(prefix[-1]*num)
        # for num in nums[::-1]:
        #     postfix.append(postfix[-1]*num)
        # postfix.reverse()
        # for i, _ in enumerate(nums):
        #     i = i+1
        #     res.append(prefix[i-1] * postfix[i])
        # return res

        #shit space complixity!
        #use res as a pre and post fix storage
        res = [1] * len(nums)
        prefix = 1
        postfix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        for i in range(len(nums) - 1, - 1,-1):
            res[i] *= postfix
            postfix *= nums[i]
        return res