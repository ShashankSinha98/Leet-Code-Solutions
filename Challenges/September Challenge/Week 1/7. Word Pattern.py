class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        sL = [i for i in s.split()]

        if len(sL)!=len(pattern):
            return False
        
        n = len(sL)
        p2s = {}
        s2p = {}
        
        for i in range(n):
            if pattern[i] not in p2s:
                p2s[pattern[i]] = sL[i]
                
            if sL[i] not in s2p:
                s2p[sL[i]] = pattern[i]
            
        for i in range(n):
            
            if p2s[pattern[i]] != sL[i]:
                return False
            
            if s2p[sL[i]] != pattern[i]:
                return False
                
        return True
            