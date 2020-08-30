class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        s = ""
        for i in digits:
            s+=str(i)
            
        n = int(s)
        
        n+=1
        
        ans = []
        for i in str(n):
            ans.append(int(i))
            
        digits = ans.copy()
        return digits
            
        