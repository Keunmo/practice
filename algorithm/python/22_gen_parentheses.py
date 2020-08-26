class Solution:
    def generateParenthesis(self, n):
        res = []
        def makebraket(open=0, close=0, braket=''):
            print('o',open,'c',close,'b',braket)
            if open < close:
                return
            if close == n:
                res.append(braket)
                return
            if open < n:
                makebraket(open+1, close, braket+'(')
            if close < n:
                makebraket(open, close+1, braket+')')
        makebraket()
        print(res)
        return res

# 1 0 (  2 0 ((  3 0 (((
#        1 1 ()  2 1 (()
#                2 1 (()
#                1 2 ())