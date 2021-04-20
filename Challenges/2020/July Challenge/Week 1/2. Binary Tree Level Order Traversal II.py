# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    d = 0
    arr = []
    h = 0
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        #print(Solution.height(self,root))
        Solution.h = Solution.height(self,root)
        Solution.arr = [[] for i in range(Solution.h)]
        Solution.printLvlOrderBottom(self,root,0)
        return Solution.arr
        
    def printLvlOrderBottom(self,root,depth): 
        
        if(root is None):
            return
        
        
        Solution.printLvlOrderBottom(self,root.left,depth+1)
        Solution.printLvlOrderBottom(self,root.right,depth+1)
        Solution.arr[Solution.h-depth-1].append(root.val)
        
    def height(self,root):
        
        if(root is None):
            return 0
        
        l = Solution.height(self,root.left)
        r = Solution.height(self,root.right)
        
        return max(l,r)+1
        