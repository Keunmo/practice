# https://leetcode.com/problems/sort-characters-by-frequency/

class Solution:
    def frequencySort(self, s: str) -> str:
        clist = list(s)
        elem = {}
        res = []
        for i in clist:
            if i in elem:
                elem[i] += 1
            else:
                elem[i] = 1
        sorted_elem = sorted(elem.items(), key = lambda x: x[1], reverse=True)
        for i in list(sorted_elem):
            res.append(i[0]*i[1])
        return ''.join(res)