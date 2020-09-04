class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        
        res = []
        i,last,lastEnd = 0,-1,0
        n = len(S)
        lastArr = [0]*256
        
        for i in range(n):
            lastArr[ord(S[i])] = i
        
        i = 0
        
        while i<n:
            lastEnd = max(lastEnd,lastArr[ord(S[i])])
            #print(i,S[i],lastEnd)
            if i==lastEnd:
                #print(i,i-last)
                res.append(i-last)
                last = i
            
            i+=1
        
        
        return res