# https://leetcode.com/problems/top-k-frequent-words/

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        if len(words) == 1:
            return words
        words.sort()
        words.append('End')
        count = 1
        lenth = len(words)
        quantity = {}
        result = []
        for i in range(lenth):
            if words[i] == 'End':
                break
            elif words[i]==words[i+1]:
                count+=1
                quantity[words[i]]=count
            else:
                quantity[words[i]]=count
                count=1
        quan_k = list(quantity.keys())
        quan_v = list(quantity.values())
        quan_v.sort()
        quan_v.reverse()
        # print(quantity)
        for i in quan_v[:k]:
            for k in quan_k:
                if quantity.get(k) == i:
                    result.append(k)
                    del quantity[k]
                    break
        return result