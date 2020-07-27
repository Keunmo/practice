# https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sumnum = 0
        for i in range(len(nums)):
            nums[i] += sumnum
            sumnum = nums[i]
        return nums