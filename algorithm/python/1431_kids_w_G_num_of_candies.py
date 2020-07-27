# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = [None]*len(candies)
        # res = []
        maxcandy = max(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies >= maxcandy:
                res[i] = True
                # res.append(True)
            else:
                res[i] = False
                # res.append(False)
        return res