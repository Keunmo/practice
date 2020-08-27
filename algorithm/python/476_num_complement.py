# https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        binum = str(bin(num)).replace('0b','')
        binum = binum.replace('1','t')
        binum = binum.replace('0','1')
        binum = binum.replace('t','0')
        return int(binum, 2)
