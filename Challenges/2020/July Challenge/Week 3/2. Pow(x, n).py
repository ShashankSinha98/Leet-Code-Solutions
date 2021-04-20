class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n>=0:
            return Solution.myPosPow(self,x,n)
        else:
            return Solution.myNegPow(self,x,abs(n))
            
    def myNegPow(self,x,n):
        if n==-1:
            return 1/x
        
        if n==0:
            return 1
        
        smallAns = Solution.myNegPow(self,x,n//2)
        smallAns = smallAns*smallAns
        
        if n%2==0:
            return smallAns
        else:
            return (1/x)*smallAns
        
        
    def myPosPow(self,x,n):
        
        if n==1:
            return x
        
        if n==0:
            return 1
        
        smallAns = Solution.myPosPow(self,x,n//2)
        smallAns = smallAns*smallAns
        
        if n&1==0:
            return smallAns
        else:
            return x*smallAns
        
        