class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        cnt = 0
        while x!=0 or y!=0:
            if (x&1 != y&1):
                cnt+=1
            x=x>>1
            y=y>>1
        
        return cnt