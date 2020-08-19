class Solution:
    def tribonacci(self, n: int) -> int:
        # tribo = [0,1,1]
        tribo0 = 0
        tribo1 = 1
        tribo2 = 1
        if n==0:
            return tribo0
        elif n==1:
            return tribo1
        elif n==2:
            return tribo2
        else:
            for i in range(n-2):
                tribo = tribo0 + tribo1 + tribo2
                tribo0, tribo1, tribo2 = tribo1, tribo2, tribo
        # for i in range(3,n+1):
        #     tribo.append(tribo[i-3]+tribo[i-2]+tribo[i-1])
        # return tribo[n]
            return tribo        
# 0 1 1 2 4 7 