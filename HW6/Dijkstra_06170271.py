from collections import defaultdict 
import math

class add_g:
    def __init__(self,start,bourn,distance):
        if add_g:
            self.s=start
            self.b=bourn
            self.d=distance
        else:
            return 
         
class Graph(): 
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
        
    def addEdge(self,u,v,w): 
        self.graph.append([u,v,w]) 

    def Dijkstra(self, s): 
        z=0
        dict={}
        tem=[]
        weight_list=[math.inf]*self.V
        for i in range(self.V):
            if i != s:
                pass
            else:
                weight_list[i]=0
            
                
                
        while len(tem) < self.V:  
            weight_list_v2 = sorted(weight_list)
            for p in range(self.V):
                if weight_list[p]==weight_list_v2[z] and p not in tem:
                    tem.append(p)
                    break
            if tem:        
                if p != 0:
                    for r in range(self.V):       
                        if weight_list[r] != math.inf:
                            if self.graph[p][r]!=0:
                                if weight_list[r] < weight_list[p]+self.graph[p][r]:
                                    pass
                                elif weight_list[r] > weight_list[p]+self.graph[p][r]:
                                    weight_list[r] = weight_list[p]+self.graph[p][r]
                                else:
                                    pass
                        else:
                            if self.graph[p][r] == 0 :
                                pass
                            elif self.graph[p][r] != 0:
                                weight_list[r]=weight_list[p]+self.graph[p][r] 
                            else:
                                pass


                elif p == 0:
                    for q in range(self.V): 
                        if weight_list[q] == math.inf:
                            if self.graph[p][q] != 0 :
                                weight_list[q] = self.graph[p][q]
                else:
                    pass


                z+=1
            
        for jkl in range(self.V):
            dict[str(jkl)]=weight_list[jkl]
        return dict
    
    def find(self, pa_node, m): 
        
        if pa_node[m] != m: 
            return self.find(pa_node, pa_node[m]) 
        elif pa_node[m] == m:
            return m
        else:
            pass 
  

    def union(self, pa_node, tem_v2, x, y): 
        
        xroot = self.find(pa_node, x) 
        yroot = self.find(pa_node, y) 
        
        if pa_node:
            
            if tem_v2[xroot] > tem_v2[yroot]: 
                pa_node[yroot] = xroot 
                
            elif tem_v2[xroot] < tem_v2[yroot]: 
                pa_node[xroot] = yroot 
                
            else : 
                pa_node[yroot] = xroot 
                tem_v2[xroot] += 1
        else:
            pass

    def Kruskal(self):
        final = dict();result =[] 
        m = 0;n = 0
        pa_node = [] ; tem_v2 = [] 
        self.graph =  sorted(self.graph,key=lambda item: item[2]) 
  
        for node in range(self.V): 
            pa_node.append(node) 
            tem_v2.append(0) 
      
        while n < self.V -1 : 

            u,v,w =  self.graph[m] 
            m = m + 1
            x = self.find(pa_node, u) ;y = self.find(pa_node ,v) 
  
            if x ==y:
                pass
            elif x != y: 
                n = n + 1     
                result.append([u,v,w]) 
                self.union(pa_node, tem_v2, x, y)
            else:
                pass
                
        for u, v, w in result:
            final[str(u)+'-'+str(v)]  = w
        return final
