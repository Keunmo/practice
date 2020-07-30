# https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        root.val = 'R'
        def inordertrav(root):
            res = []
            if root:
                if root.left and not root.right:
                    root.right = TreeNode('N')
                if not root.left and root.right:
                    root.left = TreeNode('N')
                res.append(root.val)
                return inordertrav(root.left) + res + inordertrav(root.right)
            return []
        if root.left != None and root.right != None:
            if root.left.val != root.right.val:
                return False
        node = inordertrav(root)
        # print(node)
        rootidx = node.index('R')
        left = node[:rootidx]
        right = node[rootidx+1:]
        right.reverse()
        # print(left)
        # print(right)
        return left == right



#           1
#      2        2
#   3    4    4    3
#  5 6  7 8  8 7  6 5
