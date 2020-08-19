# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
import json
class Codec:
    def serialize(self, root):
        preo = []
        def preorder(root,arr):
            if root == None:
                preo.append(-1)
                return True
            preo.append(root.val)
            preorder(root.left, preo)
            preorder(root.right, preo)
        preorder(root,[])
        return json.dumps(preo)
    index = 0
    def deserialize(self, data):
        trav = json.loads(data)
        print(trav)
        def buildTree(trav):
            if self.index == len(trav) or trav[self.index] == -1:
                self.index += 1
                return None
            root = TreeNode(trav[self.index])
            self.index += 1
            root.left = buildTree(trav)
            root.right = buildTree(trav)
            return root
        
        buildTree(trav)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))