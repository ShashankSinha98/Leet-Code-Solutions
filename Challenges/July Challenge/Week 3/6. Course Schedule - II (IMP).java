class Solution {
    
    class Graph{
        int V;
        ArrayList<ArrayList<Integer>> arr;
        
        Graph(int V){
            this.V = V;
            this.arr = new ArrayList<>();
            
            for(int i=0; i<V; i++)
                arr.add(new ArrayList<>());
        }
        
        public boolean check_cycle(){
            
            int[] visited = new int[this.V];
            int[] path = new int[this.V];
            boolean ans = false;
            for(int i=0; i<this.V; i++){
                ans = dfs(i,visited, path);
                if (ans)
                    return true;
            }
            return false;
        }
        
        public boolean dfs(int node, int[] visited,int[] path){
            
            visited[node] = 1;
            path[node] = 1;
            
            for(int c : this.arr.get(node)){
                
                if(visited[c]==0){
                 boolean cycleMila = dfs(c,visited, path);
                    if(cycleMila)
                        return true;
                } else if(visited[c]==1 && path[c]==1){
                    return true;
                }
            }
            path[node] = 0;
            return false;
        }
        
        public void add_edge(int v1, int v2){
            this.arr.get(v1).add(v2);
        }
        
        
        public void display() {
			
			for(int i=0; i<V; i++) {
				System.out.print(String.valueOf(i));
				
				for(int j=0;j<this.arr.get(i).size(); j++) {
					System.out.print(" -> "+this.arr.get(i).get(j));
				}
				System.out.println();
			}
		}
        
        public int[] topological_sort(){
            int[] visited = new int[this.V];
            LinkedList<Integer> order = new LinkedList<>();
            
            for(int i=0; i<this.V; i++){
                if(visited[i]==0){
                    dfs_helper(i,visited,order);
                }
            }
            
            int[] res = new int[this.V];
            int j=0;
            for(int i : order){
                res[j++] = i;
            }
            return res;
        }
        
        public void dfs_helper(int node, int[] visited, LinkedList<Integer> order){
            
            visited[node] = 1;
            
            for(int c : this.arr.get(node)){
                if(visited[c]==0)
                    dfs_helper(c,visited,order);
            }
            
            order.addFirst(node);
        }
        
    }
    
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        
        Graph g = new Solution().new Graph(numCourses);
        
        for(int i=0; i<prerequisites.length; i++){
            g.add_edge(prerequisites[i][1],prerequisites[i][0]);
        }
        if(g.check_cycle())
            return new int[0];
        
        return g.topological_sort();
        
    }
}