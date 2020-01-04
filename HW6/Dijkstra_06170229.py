from collections import defaultdict 
import heapq
import math

#Class to represent a graph 
class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.graph_matrix = [[0 for column in range(vertices)]
                             for row in range(vertices)]
        
    def addEdge(self,u,v,w): 
        self.graph.append([u,v,w]) 

    def Dijkstra(self, s):
        s = str(s)
        graph_dict = self.get_graph_dict()
        if not graph_dict:
            return

        pri_queue = list()
        history = set()

        heapq.heappush(pri_queue, (0, s))

        combine = {s: None}
        distance = self.get_distance(graph_dict, s)

        while len(pri_queue) > 0:
            pair = heapq.heappop(pri_queue)
            span = pair[0]
            vertex = pair[1]
            history.add(vertex)

            path_list = graph_dict[vertex].keys()
            for path in path_list:
                if path not in history:
                    new_dist = span + graph_dict[vertex][path]
                    if new_dist < distance[path]:
                        heapq.heappush(pri_queue, (new_dist, path))
                        combine[path] = vertex
                        distance[path] = new_dist

        return distance

    def get_graph_dict(self) -> dict:
        if len(self.graph) == 0:
            return

        result = {}
        for point in range(len(self.graph)):
            path_list = self.graph[point]

            data = {}
            for other, span in enumerate(path_list):
                if other == point or span == 0:
                    continue
                data[str(other)] = span

            result[str(point)] = data

        return result

    def get_distance(self, graph_dict: dict, s: str):
        result = {s: 0}
        for vertex in graph_dict.keys():
            if vertex != s:
                result[vertex] = math.inf
        return result
  

    def find(self, parent, i): 
        if parent[i] == i: 
            return i 
        return self.find(parent, parent[i]) 

    def union(self, parent, rank, x, y): 
        xroot = self.find(parent, x) 
        yroot = self.find(parent, y) 
 
        if rank[xroot] < rank[yroot]: 
            parent[xroot] = yroot 
        elif rank[xroot] > rank[yroot]: 
            parent[yroot] = xroot 
  
        else : 
            parent[yroot] = xroot 
            rank[xroot] += 1
            
    def Kruskal(self): 
        
        result =[] 
        i = 0
        e = 0
        
        self.graph =  sorted(self.graph,key=lambda item: item[2]) 
        parent = [] ; rank = [] 
        for node in range(self.V): 
            parent.append(node) 
            rank.append(0) 
            
        while e < self.V -1 : 
            u,v,w =  self.graph[i] 
            i = i + 1
            x = self.find(parent, u) 
            y = self.find(parent ,v)
            
            if x != y: 
                e = e + 1     
                result.append([u,v,w]) 
                self.union(parent, rank, x, y)  
                
        output = {}
        for u,v,weight in result: 
            u = str(u)
            v = str(v)
            output.update( {str(u+"-"+v):weight} )
        return output
