# https://leetcode.com/problems/binary-tree-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        traversal = []
        if root:
            traversal.append(root.val)
            return traversal+self.preorderTraversal(root.left)+self.preorderTraversal(root.right)
        return []
    
        # if root == None:
        #     return []
        # traversal = []
        # stack = []
        # stack.append(root)
        # while stack:
        #     node = stack.pop()
        #     traversal.append(node.val)
        #     if node.right != None:
        #         stack.append(node.right)
        #     if node.left != None:
        #         stack.append(node.left)
        # return traversal
