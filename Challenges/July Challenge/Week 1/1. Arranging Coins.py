class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        i = 1
        s = 0
        cnt = 0
        
        while s+i<=n:
            s += i
            i+=1
            cnt+=1
            
        return cnt
            
        