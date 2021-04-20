
class Solution:
    res = 0
    leftmost_pos = {}
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        global res,leftmost_pos
        res = 0
        leftmost_pos = {}
        Solution.maxWidth(self,root,0,0)
        return res
        

    def maxWidth(self,treeNode, depth,position):
        global res,leftmost_pos
        if treeNode is  None:
            return

        if depth not in leftmost_pos:
            leftmost_pos[depth] = position

        res = max(res,position-leftmost_pos[depth]+1)
        Solution.maxWidth(self,treeNode.left,depth+1,position*2)
        Solution.maxWidth(self,treeNode.right,depth+1,position*2+1)