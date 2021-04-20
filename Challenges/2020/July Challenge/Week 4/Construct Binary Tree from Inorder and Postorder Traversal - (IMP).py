# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    pIdx = -1
    
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        
        n = len(inorder)
        # Passing Solution by reference
        Solution.pIdx = n-1
        
        return Solution.buildTreeRec(self,inorder,postorder,0,n-1,n)
        
        
    def buildTreeRec(self,inorder,postorder,inSt,inEnd,n):
        
        if inSt > inEnd:
            return None
        
        node = TreeNode(postorder[Solution.pIdx])
        Solution.pIdx -= 1
        
        if inSt == inEnd:
            return node
        
        pos = -1
        for i in range(inSt,inEnd+1):
            if inorder[i] == node.val:
                pos = i
                break
        
        node.right = Solution.buildTreeRec(self,inorder,postorder,pos+1,inEnd,n)
        node.left = Solution.buildTreeRec(self,inorder,postorder,inSt,pos-1,n)
            
        return node
        
        