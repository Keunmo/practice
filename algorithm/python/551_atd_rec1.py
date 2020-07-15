# https://leetcode.com/problems/student-attendance-record-i/

class Solution:
    def checkRecord(self, s: str) -> bool:
        a = 0
        l = 0
        for i in s:
            if i == 'A':
                a+=1
                if a>1:
                    return False
            if i == 'L':
                l+=1
                if l>2:
                    return False
            else:
                l=0
        return True
                    
                
        