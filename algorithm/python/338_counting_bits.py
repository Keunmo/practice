class Solution:
    def countBits(self, num: int) -> List[int]:
        cntlist = [0]*(num+1)
        for n in range(num+1):
            for i in list(bin(n)):
                if i == '1':
                    cntlist[n]+=1
        return cntlist