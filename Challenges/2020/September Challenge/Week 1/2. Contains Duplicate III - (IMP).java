class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        
        int n = nums.length;
        
        if(n == 0 || k<0)
            return false;
        
        TreeSet<Long> set = new TreeSet<Long>();
        
        for(int i=0; i<n; i++){
            Long floor = set.floor(1L*nums[i]);
            Long ceil = set.ceiling(1L*nums[i]);
            System.out.println(floor+" , "+ceil+" , "+nums[i]);
            if(floor!=null && nums[i]-floor<=t || ceil!=null && ceil-nums[i]<=t)
                return true;
            set.add(1L*nums[i]);
            System.out.println(set);
            
            if(i>=k)
                set.remove(1L*nums[i-k]);
        }
        return false;
    }
}