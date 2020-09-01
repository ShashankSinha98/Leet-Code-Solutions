class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        total = 0
        
        for i in nums:
            total = total ^ i
                    
        
        p = total & (-total)
        
        
        first,second = 0,0
        
        for i in nums:
            if (i & p) > 0:
                first = first ^ i
        
        second = total^first
        
        return [first,second]
        