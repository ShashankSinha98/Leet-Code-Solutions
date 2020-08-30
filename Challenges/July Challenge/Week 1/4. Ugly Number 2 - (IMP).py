class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        ugly_nos = [0]*(n+1)
        ugly_nos[1] = 1
        
        i2 = i3 = i5 = 1
        
        nm_2 = 2
        nm_3 = 3
        nm_5 = 5
        
        for l in range(2,n+1):
            
            ugly_nos[l] = min(nm_2,nm_3,nm_5)
            
            if ugly_nos[l] == nm_2:
                i2+=1
                nm_2 = ugly_nos[i2]*2
                
            if ugly_nos[l] == nm_3:
                i3+=1
                nm_3 = ugly_nos[i3]*3
                
            if ugly_nos[l] == nm_5:
                i5+=1
                nm_5 = ugly_nos[i5]*5
                
        return ugly_nos[n]
        