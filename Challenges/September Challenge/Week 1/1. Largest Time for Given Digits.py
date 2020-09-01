class Solution:
    
    maxTime = [-1,-1,-1,-1]
    
    def largestTimeFromDigits(self, A: List[int]) -> str:
        
        Solution.maxTime = [-1,-1,-1,-1]
        
        Solution.getPermutations(self,A,0)
        
        res = ""
        for i in range(4):
            if i==2:
                res+=":"
            res += str(Solution.maxTime[i])
            
        
        
        return res if res != "-1-1:-1-1" else ""
    
    def compare(self,t1,t2):
        if str(t1[0])+str(t1[1])>str(t2[0])+str(t2[1]) or (str(t1[0])+str(t1[1])==str(t2[0])+str(t2[1])
        and str(t1[2])+str(t1[3])>str(t2[2])+str(t2[3])):
            return True
        else:
            return False
    
    def isValid(self,A):
        if str(A[0])+str(A[1])<"24" and str(A[2])+str(A[3])<"60":
            return True
        else:
            return False
        
    def getPermutations(self,A,idx):
        
        if idx==len(A):
            if Solution.isValid(self,A) and Solution.compare(self,A,Solution.maxTime):
                Solution.maxTime = A.copy() 
            return 
        
        for i in range(idx,len(A)):
            A[idx], A[i] = A[i], A[idx]
            Solution.getPermutations(self,A,idx+1)
            A[idx], A[i] = A[i], A[idx]
        
        