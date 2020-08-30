class Solution:
    def reverseWords(self, s: str) -> str:
        
        if len(s.strip())==0:
            return ""
        
        strArr = [i for i in s.split()]
        i,j = 0,len(strArr)-1
        
        while(i<=j):
            strArr[i],strArr[j] = strArr[j],strArr[i]
            i+=1
            j-=1
            

        res = ""
        for i in strArr[0:-1]:
            res+=i+" "
        res+=strArr[-1]
        return res
        