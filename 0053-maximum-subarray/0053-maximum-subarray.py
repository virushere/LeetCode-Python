class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsub = nums[0]
        currSum = 0

        for n in nums:
            if currSum < 0:
                currSum = 0
            currSum += n
            maxsub = max(maxsub, currSum)
        return maxsub