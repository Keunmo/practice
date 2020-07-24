# https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cut = len(nums) // 3
        elem = {}
        res = []
        for i in nums:
            if i in elem:
                elem[i] += 1
            else:
                elem[i] = 1
        for i in list(elem.items()):
            if i[1] > cut:
                res.append(i[0])
        return res