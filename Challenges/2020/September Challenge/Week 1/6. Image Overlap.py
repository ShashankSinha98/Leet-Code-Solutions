class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        
        maxOverlap = 0
        n = len(A)
        
        for col in range(-n+1,n):
            for row in range(-n+1,n):
                maxOverlap = max(maxOverlap,Solution.countOverlap(A,B,row,col,n))
                
        return maxOverlap
    
    
    def countOverlap(A,B,row,col,n):
        
        count = 0
        rs,re,cs,ce = 0,0,0,0
        
        if row<=0:
            rs,re = 0,row+n-1
        else:
            rs,re = row,n-1
            
        if col<=0:
            cs,ce = 0,col+n-1
        else:
            cs,ce = col,n-1
            
        for r in range(rs,re+1):
            for c in range(cs,ce+1):
                rowdiff = n-(re-rs)-1
                if rs!=0:
                    rowdiff = -1*rowdiff
                rb = rowdiff + r
                
                coldiff = n-(ce-cs)-1
                if cs!=0:
                    coldiff = -1*coldiff
                cb = coldiff + c
                
                if A[r][c]==1 and B[rb][cb]==1:
                    count+=1
                
            
        return count
        
        