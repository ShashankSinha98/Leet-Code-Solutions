class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        n = len(nums)
        nums.sort()
        
        for i in range(0,n-2):
            one = nums[i]
            l = i+1
            r = n-1
            if i==0 or nums[i]!=nums[i-1]:
                while(l<r):

                    if one+nums[l]+nums[r]==0:
                        res.append([one,nums[l],nums[r]])
                        l+=1
                        
                        while l<r and nums[l]==nums[l-1]:
                            l+=1
                        while l<r and nums[r]==nums[r-1]:
                            r-=1

                    elif one+nums[l]+nums[r]<0:
                        l+=1
                    else:
                        r-=1
                    
        return res
                
        