class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        n = len(s)
        
        for i in range(2,n+1):
            sub = s[0:n//i]
            
            if sub*i == s:
                return True
        
        return False
        