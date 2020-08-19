class Solution:
    anslist = []
    sqrlist = []
    def notperfSquares(self, n, lastmax):
        ans = 0
        ptr = n
        pin = n
        self.sqrlist = []
        while True:
            # print('---')
            # print('ptr',ptr)
            # print('l.m',lastmax)
            sqrt = ptr**0.5
            if ptr == 0:
                break
            if ptr == lastmax:
                ptr -= 1
                continue
            if sqrt == int(sqrt):
                # print('poo  *')
                self.sqrlist.append(ptr)
                ans+=1
                ptr = pin - ptr
                pin = ptr
            else:
                ptr -= 1
        if ans != 0:
            self.anslist.append(ans)
        # print('a.l',self.anslist)
        return ans

    def numSquares(self, n: int) -> int:
        if n**0.5 == int(n**0.5):
            # print(1)
            return 1
        else:
            self.anslist = []
            iternum = self.notperfSquares(n,0)
            for i in range(iternum-1):
                if self.sqrlist:
                    lastmax = max(self.sqrlist)
                else:
                    lastmax = 0
                # print('i.n',iternum)
                # print('l.m',lastmax)
                # print(self.sqrlist)
                self.notperfSquares(n,lastmax)
            while 1 in self.anslist:
                self.anslist.remove(1)
            print(min(self.anslist))
            return min(self.anslist)
    
sol = Solution()
sol.numSquares(43)

# 43

# 36 4 1 1 1
#  7 3 2 1 0

# 25 16 1 1 
# 18 2  1 0

# 25 9 9 
# 18 9 0