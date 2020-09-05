# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        A = []
        Solution.getSorted(self,root1,A)
        B = []
        Solution.getSorted(self,root2,B)
        print(A,B)
        al,bl = len(A),len(B)
        res = []
        i,j=0,0
        
        while i<al and j<bl:
            if A[i]<B[j]:
                res.append(A[i])
                i+=1
            else:
                res.append(B[j])
                j+=1
                
        while i<al:
            res.append(A[i])
            i+=1
            
        while j<bl:
            res.append(B[j])
            j+=1
        
        return res
        
    def getSorted(self,root,L):
        
        if root==None:
            return
        
        Solution.getSorted(self,root.left,L)
        L.append(root.val)
        Solution.getSorted(self,root.right,L)
        
        