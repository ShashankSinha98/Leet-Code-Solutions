class Solution:
    def isHappy(self, n: int) -> bool:
        
        
        while True:
            temp = n
            res = 0
            while(temp!=0):
                res += (temp%10)*(temp%10)
                temp//=10
            n = res
            #print(n)
            
            if(n<10):
                break
            
            
            
        return (n==1 or n==7)
                
        