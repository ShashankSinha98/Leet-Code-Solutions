import sys
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        prevMaxProd = nums[0]
        prevMinProd = nums[0]
        MaxProd = nums[0]
        
        for i in range(1,len(nums)):
            currMax = max(prevMaxProd*nums[i],prevMinProd*nums[i],nums[i])
            currMin = min(prevMaxProd*nums[i],prevMinProd*nums[i],nums[i])
            
            MaxProd = max(MaxProd,currMax)
            
            prevMaxProd = currMax
            prevMinProd = currMin
            
        return MaxProd
            