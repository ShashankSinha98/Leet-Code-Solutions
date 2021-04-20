import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        
        maxSoFar = 0
        maxRes = -sys.maxsize
        
        for i in range(len(nums)):
            maxSoFar += nums[i]
            
            
            
            if maxRes<maxSoFar:
                maxRes = maxSoFar
                
            if maxSoFar<0:
                maxSoFar = 0
            
                
        return maxRes

        