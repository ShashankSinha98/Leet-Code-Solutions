class Solution:
    
    def binToDec(self,b: str):
        res=0
        t = 1
        while b!="":
            if b[-1]=="1":
                res+=t
            t=t*2
            b=b[0:-1]
        return res
    
    def decToBin(self,n: int):
        if n==0:
            return "0"
        
        res = ""
        
        
        while n!=0:
            if n&1==1:
                res = "1"+res
            else:
                res = "0"+res
            n=n>>1
        return res
            
    
    def addBinary(self, a: str, b: str) -> str:
        int_a = Solution.binToDec(self,a)
        int_b = Solution.binToDec(self,b)
        
        int_res = int_a + int_b
        return Solution.decToBin(self,int_res)
        
                    
                
            
            
        
        
        