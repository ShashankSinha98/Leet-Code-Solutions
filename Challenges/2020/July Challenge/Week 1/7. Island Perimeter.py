class Solution:
    
    def check_para(self,grid,i,j,h,w):
        res = 0
        # Checking Top(i-1,j)
        if(i-1<0 or (i-1>=0 and grid[i-1][j]==0)):
            res+=1
            
        # Checking Bottom(i+1,j)
        if(i+1>=h or (i+1<h and grid[i+1][j]==0)):
            res+=1
            
        # Checking left(i,j-1)
        if(j-1<0 or (j-1>=0 and grid[i][j-1]==0)):
            res+=1
            
        # Checking Right(i,j+1)
        if(j+1>=w or (j+1<w and grid[i][j+1]==0)):
            res+=1
        
        return res
    
    
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        res = 0
        h = len(grid)
        w = len(grid[0])
        
        for i in range(h):
            for j in range(w):
                if grid[i][j]==1:
                    r = Solution.check_para(self,grid,i,j,h,w)
                    #print(i,j,r)
                    res+=r
                
        return res
        
        