from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        l = 0
        r = n-1
        
        while(l<=r):
            
            if l==r:
                return nums[l]
            
            mid = (l+r)//2
            
            if nums[mid]<nums[r]:
                r = mid
            else:
                l = mid + 1
            
        return -1
        
arr = [4,5,1,2,3]
s = Solution()

ans = s.findMin(arr)
print(ans)