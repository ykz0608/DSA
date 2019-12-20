from collections import defaultdict 

class Graph:
    def __init__(self): 
        self.graph = defaultdict(list) 

    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    def BFS(self, s): 
        queue = [] 
        output = []
        if len(output)==0:
            output.append(s)
            queue.extend(self.graph[s])  
        
        while len(queue) != 0 :   
            vertex = queue[0]
            output.append(vertex)
            queue.pop(0)
            for i in self.graph[vertex]:
                if i not in queue and i not in output:
                    queue.append(i)
        return output
        
    def DFS(self, s): 
        queue = [] 
        output = []
        if len(output)==0:
            output.append(s)
            queue.extend(self.graph[s])  
        
        while len(queue) != 0 :   
            vertex = queue[-1]
            output.append(vertex)
            queue.pop(-1)
            for i in self.graph[vertex]:
                if i not in queue and i not in output:
                    queue.append(i)
        return output
      

