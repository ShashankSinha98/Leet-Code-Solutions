class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        n = len(nums)
        l = 0
        r = n-1
        
        while (l<=r):
            
            if l==r:
                return nums[l]
            
            m = (l+r)//2
            
            if nums[m]>nums[r]:
                l = m+1
            elif nums[m]<nums[l]:
                r = m
            else:
                r = r-1
                
        return -1
        