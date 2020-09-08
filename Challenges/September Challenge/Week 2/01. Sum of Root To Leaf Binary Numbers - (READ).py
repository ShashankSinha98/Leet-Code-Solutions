# https://www.youtube.com/watch?v=Wj4mLZ7XW0A

class Solution:
    
    final_sum = 0
    
    def sumRootToLeaf(self, root: TreeNode) -> int:
        
        Solution.final_sum = 0
        Solution.helper(self,root,[])
        
        return Solution.final_sum
        
        
    def helper(self,root,value):
        
        if root == None:
            return
        
        if root.left==None and root.right==None:
            value+=[root.val]
            Solution.final_sum+=Solution.decToBin(self,value)
            value = value.pop()
            return
        
        value.append(root.val)
        Solution.helper(self,root.left,value)
        Solution.helper(self,root.right,value)
        value.pop()
        
    def decToBin(self,arr):
        
        n = len(arr)
        res = 0
        
        for i in range(n):
            res+=(2**i)*arr[n-i-1]
        
        return res
        