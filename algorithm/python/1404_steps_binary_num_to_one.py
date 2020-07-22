# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/

class Solution:
    def numSteps(self, s: str) -> int:
        count = 0
        ints = int('0b'+s,2)
        while ints != 1:
            count += 1
            if ints % 2:
                ints += 1
            else:
                ints = ints // 2
        return count
