

from collections import defaultdict 
  
class Graph:
    
    def __init__(self): 
        
        self.graph = defaultdict(list) 

    
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
   
    def BFS(self, s): 
        
        visited = [s] 
        queue = [s] 
        
        while queue:
            s = queue.pop(0)
            for neighbor in self.graph[s]:
                    if neighbor not in visited:
                        visited.append(neighbor)
                        queue.append(neighbor)
        return visited
    
    def DFS(self, s):
        
        visited = []
        stack = [s]
        
        while stack:
            s = stack.pop()
            visited.append(s)
        
            for neighbor in self.graph[s]:
                if neighbor not in visited:
                        stack.append(neighbor) 
        return visited
        

