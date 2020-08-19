# https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        if len(S)==0:
            return None
        lvlist=[]   # list of tuple (level, node)
        lv = 1
        S=S.split('-')
        node = TreeNode(S[0])
        lvlist.append((0,node)) 
        # manually append 1st elem in lvlist because, 
        # this code calc lv by count non-digit elem(==''), but when do S.split(), 1st elem(lv 0) and 2nd elem(lv 1)'s whitespace is same.
        # so it start iter at 2nd elem, and lv starts at 1.
        for i in S[1:]:
            if i.isdigit():
                node = TreeNode(i)
                lvlist.append((lv,node))
                lv=1
            else:
                lv+=1
        stk=[]
        stk.append(lvlist[0])
        # append 1st elem at stack manually because for loop compare elem with stk's top.
        for i in lvlist[1:]:
            if stk[-1][0] + 1 == i[0]:      #stk top lv+1 == i lv
                stk[-1][1].left = i[1]      #stk top node.left = i node. bc it is 1st child.
                stk.append(i)
            else:
                while not stk[-1][0] + 1 == i[0]:   #pop unntil stk top lv+1 == i lv. ==pop until parent node become stk's top.
                    stk.pop()
                stk[-1][1].right = i[1]     #stk top node.right = i node. bc it must be 2nd child.
                stk.append(i)
        return lvlist[0][1]                 #return root node.

            
            
            
            