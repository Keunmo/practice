# https://leetcode.com/problems/maximum-score-after-splitting-a-string/

class Solution:
    def maxScore(self, s: str) -> int:
        left = ''
        right = ''
        score = 0
        sclist = []
        for i in range(len(s)-1):
            left = s[:i+1]
            right = s[i+1:]
            for i in left:
                if i == '0':
                    score+=1
            for i in right:
                if i == '1':
                    score+=1
            sclist.append(score)
            score = 0
        return max(sclist)