# https://leetcode.com/problems/monotonic-array/

class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        b = A[:]
        b.sort()
        c = b[:]
        c.reverse()
        if A == b:
            return True
        elif A == c:
            return True
        return False
            