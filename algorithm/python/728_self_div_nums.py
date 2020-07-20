# https://leetcode.com/problems/self-dividing-numbers/

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        nums = []
        result = []
        
        def loop(s):
            for j in s:
                if j == '0':
                    return False
                if i % int(j) != 0:
                    return False
            return True
        
        for i in range(right):
            nums.append(i+1)
        nums = nums[left-1:]
        for i in nums:
            s = str(i)
            if loop(s):
                result.append(i)
        return result