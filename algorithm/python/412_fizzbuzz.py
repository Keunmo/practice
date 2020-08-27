# https://leetcode.com/problems/fizz-buzz/

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1,n+1):
            out = ''
            if i%3==0:
                out+='Fizz'
            if i%5==0:
                out+='Buzz'
            if i%3!=0 and i%5!=0:
                out = str(i)
            res.append(out)
        return res
