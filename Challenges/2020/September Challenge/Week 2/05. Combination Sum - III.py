class Solution:
    
    ret = []
    
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        if n>45:
            return []
        
        Solution.ret = []
        Solution.solve(self,k,n,[],1)
        return Solution.ret
    
    def solve(self,k,target,arr,no):
        
        if target==0 and k==0:
            Solution.ret.append(arr.copy())
            return
        
        if target<0 or k==0 or no==10:
            return
        
        for i in range(no,10):
            arr += [i]
            Solution.solve(self,k-1,target-i,arr,i+1)
            arr.remove(i)
    