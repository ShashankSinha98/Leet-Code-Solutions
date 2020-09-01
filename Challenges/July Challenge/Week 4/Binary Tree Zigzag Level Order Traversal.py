# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        return Solution.solve(self,root)
    
    def height(self,root):
        
        if root is None:
            return 0
        
        return max(Solution.height(self,root.left),Solution.height(self,root.right))+1
        
        
    def solve(self,root):
        s1 = []
        s1.append(root)
        s2 = []
        res = []
        
        h = Solution.height(self,root)
        
        for order in range(h):
            temp = []

            if order%2==0:
                while len(s1)!=0:

                    t = s1.pop()
                    temp.append(t.val)
                    if t.left is not None:
                        s2.append(t.left)

                    if t.right is not None:
                        s2.append(t.right)
            else:
                while len(s2)!=0:

                    t = s2.pop()
                    temp.append(t.val)
                    if t.right is not None:
                        s1.append(t.right)

                    if t.left is not None:
                        s1.append(t.left)
            res.append(temp)
            
        return res

        
        
        
        