class Solution:
    def maximum69Number (self, num: int) -> int:
        numl = list(str(num))
        for i in range(len(numl)):
            if numl[i] == '6':
                numl[i] = '9'
                break
        return int(''.join(numl))
        
