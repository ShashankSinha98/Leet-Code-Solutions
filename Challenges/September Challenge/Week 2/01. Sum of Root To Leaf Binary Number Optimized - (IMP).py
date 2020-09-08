# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def helper(self,node,res):
        
        if node==None:
            return 0
        
        res = (res<<1)+node.val
        
        if node.left==None and node.right==None:
            return res
        
        
        return Solution.helper(self,node.left,res) + Solution.helper(self,node.right,res)
    
    def sumRootToLeaf(self, root: TreeNode) -> int:
        
        return Solution.helper(self,root,0)
        
        
        