# https://leetcode.com/problems/number-of-good-pairs/

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good = 0
        for i in range(len(nums)):
            for j in range(len(nums[i+1:])):
                # print('i',nums[i],'j',nums[j+i+1])
                if nums[i] == nums[j+i+1]:
                    good += 1
        return good