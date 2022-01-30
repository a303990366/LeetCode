# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.tmp=[]
    def inorderTraversal(self, root):
        if root:
            
            if root.left:
                self.inorderTraversal(root.left)
            self.tmp.append(root.val)
            if root.right:
                self.inorderTraversal(root.right)
            return self.tmp
        
                
