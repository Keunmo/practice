# https://leetcode.com/problems/validate-binary-search-tree/

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def inOrderTrav(root):
            inorder = []
            if root:
                inorder.append(root.val)
                return inOrderTrav(root.left) + inorder + inOrderTrav(root.right)
            return []
        
        def maxmin(root,sel):
            if root:
                inorder = inOrderTrav(root)
                # print(rootval)
                # print(inorder)
            if sel == 0:
                return min(inorder)
            if sel == 1:
                return max(inorder)
                    
        if root == None:
            return True
        if root.left != None and not (maxmin(root.left,1) < root.val):
            return False
        if root.right != None and not (root.val < maxmin(root.right,0)):
            return False
        if not self.isValidBST(root.left) or not self.isValidBST(root.right):
            return False
        return True