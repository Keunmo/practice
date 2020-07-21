# https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums
        nums.sort()
        nums.append('End')
        count = 1
        lenth = len(nums)
        quantity = {}
        result = []
        for i in range(lenth):
            if nums[i] == 'End':
                break
            elif nums[i]==nums[i+1]:
                count+=1
                quantity[nums[i]]=count
            else:
                quantity[nums[i]]=count
                count=1
        quan_k = list(quantity.keys())
        quan_v = list(quantity.values())
        quan_v.sort()
        quan_v.reverse()
        # print(quantity)
        for i in quan_v[:k]:
            for k in quan_k:
                if quantity.get(k) == i:
                    result.append(k)
                    del quantity[k]
                    break
        return result

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums
        nums.sort()
        quantity = {}
        res = []
        for i in nums:
            if i in quantity:
                quantity[i] += 1 
            else:
                quantity[i] = 1
        top_item = sorted(quantity.items(), key=lambda x: x[1], reverse=True)
        for i in top_item[:k]:
            res.append(i[0])
        return res