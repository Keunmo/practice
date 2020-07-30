# https://leetcode.com/problems/combination-sum-iii/

def combinationSum3(k: int, n: int):
    numlist = [i for i in range(1,10)]
    if sum(numlist[-k:]) < n:
        return []
    
    def doublecomb(n):
        a = 0
        res = []
        while a<=9:
            a+=1
            b = n-a
            if a>=b:
                break
            res.append([a,b])
        return res
 
    def updatecomb(combs, elem):
        res = []
        combs.remove(elem)
        maxval = max(combs)
        for i in doublecomb(elem):
            if maxval < min(i):
                res.append(combs+i)
        return res
    
    if k == 2:
        print(doublecomb(n))
        return doublecomb(n)
    
    res = doublecomb(n)
    print('res:',res)
    while k > 2:
        print('k:',k)
        k -= 1
        reslen = len(res)
        for i in range(reslen):
            print('i',i)
            print('changetarget',res[0])
            res = res + updatecomb(res[0],max(res[0]))
            res = res[1:]
            print(res)
    print(res)
    res = [x for x in res if max(x)<10]
    print(res)

combinationSum3(2,9)
