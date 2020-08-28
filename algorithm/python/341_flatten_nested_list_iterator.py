# https://leetcode.com/problems/flatten-nested-list-iterator/

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.ptr = 0
        # self.nl = nestedList
        self.flatten = []
        # print(nestedList)
        num = ''
        for i in str(nestedList):
            if i.isdigit() or i == '-':
                num += i
            else:
                if num != '':
                    self.flatten.append(int(num))
                num = ''

    def next(self) -> int:
#         n = self.nl[self.ptr]
#         if n.isInteger():
#             self.ptr += 1
#             self.flatten.pop(0)
#             return n.getInteger()
#         else:
#             nlist = n.getList()
#             return nlist
        out = self.flatten[self.ptr]
        self.ptr += 1
        return out

    def hasNext(self) -> bool:
        
        if self.ptr < len(self.flatten):
            return True
        else:
            return False
# [[1,1],2,[1,1]]
# [NestedInteger{_integer: None, _list: [NestedInteger{_integer: 1, _list: []}, NestedInteger{_integer: 1, _list: []}]}, 
#  NestedInteger{_integer: 2, _list: []}, 
#  NestedInteger{_integer: None, _list: [NestedInteger{_integer: 1, _list: []}, NestedInteger{_integer: 1, _list: []}]}]

# [1,[4,[6]]]
# [NI{_int: 1, _list: []}, 
#  NI{_int: None, _list: [NI{_int: 4, _list: []}, NI{_int: None, _list: [NI{_int: 6, _list: []}]}]}]
# [1, 4, 6]

# [1,[2,[3,[4]]]]
# [NestedInteger{_integer: 1, _list: []}, 
# NestedInteger{_integer: None, _list: [NestedInteger{_integer: 2, _list: []}, NestedInteger{_integer: None, _list: [NestedInteger{_integer: 3, _list: []}, NestedInteger{_integer: None, _list: [NestedInteger{_integer: 4, _list: []}]}]}]}]


        
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
